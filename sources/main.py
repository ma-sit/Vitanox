import sys
import json
from shared.components.config import *
from interface.menu import bouton, dessiner_menu, plein_ecran
from interface.menu import bouton,dessiner_menu, plein_ecran
from interface.selection_niveau import selection_niveau
from interface.parametres import page_parametres

@@ -24,6 +24,41 @@
        'Quitter': K_q
    }

# Boucle principale
act = True
while act:
    dessiner_menu(ecr)
    
    for evt in event.get():
        if evt.type == QUIT:
            act = False
        if evt.type == MOUSEBUTTONDOWN and evt.button == 1:
            if btn_jeu["rect"].collidepoint(evt.pos):
                son_clicmenu.play()
                act = selection_niveau()
            elif btn_cfg["rect"].collidepoint(evt.pos):
                son_clicmenu.play()
                act = page_parametres()
            elif btn_fin["rect"].collidepoint(evt.pos):
                son_clicmenu.play()
                act = False
        if evt.type == KEYDOWN:
            if evt.key == touches['Plein écran']:
                plein_ecran()
            elif evt.key == touches['Jouer']:
                act = selection_niveau()
            elif evt.key == touches['Paramètres']:
                act = page_parametres()
            elif evt.key == touches['Quitter']:
                act = False
    display.flip()
    time.delay(30)
quit()
sys.exit()
# Boucle principale
act = True
while act:
