# LessonUp-kanalen: mockup

Mockup van [lessonup.com/nl/channels](https://www.lessonup.com/nl/channels) met een schakelaar tussen **partnerkanalen** en **LessonUp Originals**.

- Live: https://gsleraar-hue.github.io/lessonup-kanalen-mockup/
- Direct naar Originals: `…/#originals`
- Beheer (Originals en Uitgelicht aanwijzen): `…/#beheer`

## Bestanden

| Bestand | Wat |
|---|---|
| `index.html` | De pagina (gebouwd uit `src/template.html` met `python src/build.py`) |
| `channels.json` | Alle kanalen zoals op lessonup.com (naam, ondertitel, afbeeldingen) |
| `config.json` | Welke kanalen Originals zijn en welke uitgelicht zijn. Wordt bijgewerkt via het beheerscherm |

## Publiceren vanuit beheer

Het beheerscherm schrijft `config.json` via de GitHub API. Daarvoor is een fine-grained token nodig met alleen toegang tot deze repo en *Contents: Read and write*. Het token blijft in de browser van de beheerder (localStorage). Zonder token kun je `config.json` downloaden en hier handmatig vervangen.
