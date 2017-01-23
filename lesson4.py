Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> players = [02, 12, 26, 54, 66, 100]
SyntaxError: invalid token
>>> players = [2, 12, 26, 54, 66, 100]
>>> players[2]
26
>>> players[2] = 45
>>> players
[2, 12, 45, 54, 66, 100]
>>> players + [90, 91, 98]
[2, 12, 45, 54, 66, 100, 90, 91, 98]
>>> players.append(34)
>>> players
[2, 12, 45, 54, 66, 100, 34]
>>> players[:2]
[2, 12]
>>> players[:2] = [10, 0]
>>> players
[10, 0, 45, 54, 66, 100, 34]
>>> players[:2] = []
>>> players
[45, 54, 66, 100, 34]
>>> players[:] = []
>>> players
[]
>>> 
