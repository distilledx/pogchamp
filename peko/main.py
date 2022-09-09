# -*- coding: utf-8 -*-

import random
import re

def pekify(string: str):
	l = re.findall(r'([\s\S]*?[!.?"])|([\s\S]*?$)', string, flags=re.IGNORECASE)
	l = [(i[0] or i[1]).strip() for i in l]
	l = [i for i in l if i]

	#print(l)

	for i in range(len(l)):
		l[i] = l[i].strip()

		if (len(''.join([th for th in l[i] if th.isalpha()])) < 5) and (len(l) > 1):
			continue

		if l[i][-1] in ('!', '.', '?', '"'):
			if l[i][-1:-3:-1].isupper():
				l[i] = l[i][0:-1] + ' PEKO' + l[i][-1]
			else:
				l[i] = l[i][0:-1] + ' peko' + l[i][-1]
		else:
			if l[i].isupper():
				l[i] = l[i][0::] + ' PEKO'
			else:
				l[i] = l[i][0::] + ' peko'

	sentences = {}

	for j in enumerate(l):
		a = j[1].split(' ')
		a_changed = []
		for x in a:
			if (len(''.join([th for th in x if th.isalpha()])) > 4) and (x.isascii()):
				if x[-1].lower() in ('c', 'd', 'k', 'p', 't'):
					if x.isupper():
						x += '-O'
					else:
						x += '-o'

				if 'ec' in x.lower()[0:2]:
					if x.isupper():
						x = x.replace(x[0:x.lower().index('ec')+2], 'PEK')
					else:
						x = x.replace(x[0:x.lower().index('ec')+2], 'pek')

				if 'ek' in x.lower()[0:2]:
					if x.isupper():
						x = x.replace(x[0:x.lower().index('ek')+2], 'PEK')
					else:
						x = x.replace(x[0:x.lower().index('ek')+2], 'pek')

				if x.lower().startswith('ex'):
					if x.isupper():
						x = 'PEKS' + x[2::]
					else:
						x = 'peks' + x[2::]

				if 'o' in x.lower()[0:2]:
					try:
						if x.isupper():
							x = x.replace(x[0:x.lower().index('O')+1], 'PEKO')
						else:
							x = x.replace(x[0:x.lower().index('o')+1], 'peko')
					except:
						pass

			a_changed.append(x)

		to_add = ' '.join(a_changed)
		if len(to_add) > 4:
			sentences[j[0]] = ' '.join(a_changed) + ' '
		else:
			sentences[j[0]] = ' '.join(a_changed)

	final = ''

	for i in sentences.values():
		final += i

	return final.replace('  ', ' ')

#old, newprint(pekify('His screams echoed through the building, holding most unsuspecting people\'s attentions for a second, before it was forgotten. She stood over his crumpled body, a condescending look on her face. Accusingly she pointed at the figure holding his groin at her feet and yelled "ANAL SEX DEMON!". This time an even sharper shriek was heard, a tone usually reserved for women in horror movies. It was the boy standing behind her. He fearfully covered his mouth and faintly mumbled "anal..sex.. demon...?" She kicked the figure in front of her once more, and the crumpled boy let out another burst of whimpers. There was no doubt anymore. The people in the class were first filled with fear, then denial, but finally, vengeance. The unforgivingly walked towards the huddled up boy to exercise their god given right. Each one, without halt, drove their feet into the boy\'s crotch. Some approaching with the tips of their spiked cleats, others with the heels of their stilettos. The boy would later thank them for their strong willed service to helping him and the society by exorcising him. For now all he could do was lay on the floor with his eyes rolled back, covered in welts and bruises, effectively castrated for the rest of his life. The group finally let out a breath of relief. Cheers were had around the sombre scene, high fives all around. They had just saved this boy\'s life, whether he would realize it or not.'))
#print(pekify('"anal...sex...demon?"'))
