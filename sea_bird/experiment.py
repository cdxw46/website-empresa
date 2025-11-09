text = "ERIN CHarc de Oriomphex Be Feliancez top of your gamez undefeated with G ME winsz biggest competition is sea bird but it seems like you have a good chance of winningx ictfQfrenchjhorsesjdeservejmorejlovejtooK Face starts and that lunatic sea bird veers off into the far corner and is trapped somewhere in the middle of the packx Lou manage to take the lead at the the final cornerz plenty of energy impossible to lose nowxxx But out of nowhere comes sea bird xxx who then beats you by I lengthsqJq Place And beating third by another N lengthsx Do embarrassed that you retire immediatelyx"
mapping = {
    'E': 'e',
    'R': 'v',
    'I': 'e',
    'N': 'n',
}
translated = ''.join(mapping.get(ch, ch) for ch in text)
print(translated)
