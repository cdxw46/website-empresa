import json
from pwn import remote

from hamiltonicity_bc3acea59e37dd6941ddd4fdbf34f5ff import (
    commit_to_graph,
    permute_graph,
    hash_committed_graph,
    comm_params,
    get_r_vals,
)


HOST = "archive.cryptohack.org"
PORT = 34597


def main():
    numrounds = 128
    N = 5
    cycle = [(0, 4), (4, 2), (2, 3), (3, 1), (1, 0)]
    G = [
        [0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
    ]

    with remote(HOST, PORT) as conn:
        conn.recvuntil(b"prove to me that G has a hamiltonian cycle!")

        A_vars = []
        opening_vars = []
        permutation_vars = []
        FS_state = b""

        for _ in range(numrounds):
            A, openings = commit_to_graph(G, N)
            permutation = list(range(N))
            A_permuted = permute_graph(A, N, permutation)
            A_vars.append(A_permuted)
            opening_vars.append(openings)
            permutation_vars.append(permutation)

        for A in A_vars:
            FS_state = hash_committed_graph(A, FS_state, comm_params)

        challenge_bits = bin(int.from_bytes(FS_state, "big"))[-numrounds:]
        challenge_bits = challenge_bits.rjust(numrounds, "0")

        proofs = []
        for i in range(numrounds):
            challenge = int(challenge_bits[i])
            A = A_vars[i]
            openings = opening_vars[i]
            permutation = permutation_vars[i]

            if challenge:
                permuted_cycle = []
                for x in cycle:
                    permuted_cycle.append([permutation.index(x[0]), permutation.index(x[1])])
                r_vals = get_r_vals(openings, N, cycle)
                z = [permuted_cycle, r_vals]
            else:
                z = [permutation, openings]

            proofs.append(json.dumps({"A": A, "z": z}))

        for proof in proofs:
            conn.recvuntil(b"send fiat shamir proof: ")
            conn.sendline(proof.encode())

        conn.interactive()


if __name__ == "__main__":
    main()

