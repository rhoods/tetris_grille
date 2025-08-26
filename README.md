Usage comme librairie Python
===========================

Installation locale (editable):

```bash
pip install -e .
```

Depuis un autre projet:

```python
import tetris_grille as tg

# Lance le jeu
tg.run_game()
```

Notes d’intégration:
- Les assets (images, sons, polices, score) sont inclus dans le paquet et chargés via `tetris_grille.resources.get_asset_path`.
- Le module n’exécute plus le jeu à l’import; utilisez `tg.run_game()`.