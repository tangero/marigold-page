---
author: Marisa Aigen
category: retro hardware
companies:
- Apple
- Amiga
- Atari
date: '2025-11-16 06:00:00'
description: 'Komunita nadšenců pro retro počítače dosáhla historického milníku: poprvé
  v historii byl Macintosh s procesorem Motorola 68060 úspěšně rozjedán. Tím padá
  dlouholeté tvrzení fanoušků Amigy a Atari, že jejich systémy byly rychlejší než
  Macintosh.'
importance: 3
layout: tech_news_article
original_title: The Fastest (68k) Macintosh Might Not Be An Amiga Anymore - Hackaday
publishedAt: '2025-11-16T06:00:00+00:00'
slug: the-fastest-68k-macintosh-might-not-be-an-amiga-an
source:
  emoji: 📰
  id: null
  name: Hackaday
title: Nejrychlejší (68k) Macintosh už nemusí být Amiga
url: https://hackaday.com/2025/11/15/the-fastest-68k-macintosh-might-not-be-an-amiga-anymore/
urlToImage: https://hackaday.com/wp-content/uploads/2025/11/Mac68060-e1763156374360.jpg
urlToImageBackup: https://hackaday.com/wp-content/uploads/2025/11/Mac68060-e1763156374360.jpg
---

## Souhrn
Po desítkách let technologické nostalgie se podařilo entuziastovi s přezdívkou [zigzagjoe] rozjet Macintosh Quadra 650 s procesorem Motorola 68060 – nejvýkonnějším čipem řady 68k. Tím se naplnil dlouholetý sen komunity a zároveň byl vyvrácen mýtus, že nejrychlejší Macintosh běžel na Amize nebo Atari.

## Klíčové body
- První úspěšné spuštění Macintoshu s procesorem 68060 v historii
- Využití adaptéru mezi 68040 a 68060 od vývojáře [Reinauer]
- Nutnost úpravy ROM kvůli nekompatibilitě instrukční sady mezi 68040 a 68060
- Stabilní provoz pouze při snížené frekvenci na 50 MHz kvůli problémům s branch prediction
- Úspěšné spuštění hry DOOM jako praktického testu výkonu

## Podrobnosti
Macintosh Quadra 650 původně využíval procesor Motorola 68040 taktovaný na 25 MHz. Zatímco konkurenční platformy jako Amiga nebo Atari mohly díky akcelerátorským kartám využívat výkonnější 68060, Apple nikdy tento čip do svých počítačů nezačlenil – přešel přímo na PowerPC. Nyní se podařilo tento mezeru uzavřít retroinženýrstvím. Problém nebyl jen hardwarový – procesory 68040 a 68060 nejsou pinově kompatibilní, což vyřešil [Reinauer] vývojem speciálního socket adaptéru. Větší výzvou byla ale softwareová nekompatibilita: instrukční sada 68060 není plně zpětně kompatibilní s 68040. [zigzagjoe] proto vytvořil vlastní ROM, která obsahuje překladač chybějících instrukcí, což umožnilo spustit systém System 7.1 – poslední verzi, která na této architektuře funguje. Při testování se ukázalo, že plná frekvence 66 MHz je nestabilní, a proto byl procesor přetaktován na 50 MHz s aktivní branch prediction. I tak jde o dvojnásobné zrychlení oproti původnímu 25 MHz. Jako benchmark byla použita hra DOOM: při 66 MHz bez branch prediction dosáhla 16,4 FPS, při 50 MHz s branch prediction pak 14,3 FPS.

## Proč je to důležité
Tento projekt nemá praktický dopad na současnou technologii, ale představuje významný milník v komunitě retro hardwaru. Dokazuje, že i po třiceti letech lze překonávat původní omezení výrobců a dosahovat toho, co tehdejší inženýři nepovažovali za možné. Zároveň ilustruje rozdíly mezi dnešním přístupem k zpětné kompatibilitě (např. v x86) a historickou realitou, kdy výrobci často obětovali kompatibilitu ve prospěch výkonu. Pro nadšence jde o triumf technického ducha a připomínku, že historie počítačů není uzavřená – stále se dá přepisovat.

---

[Číst původní článek](https://hackaday.com/2025/11/15/the-fastest-68k-macintosh-might-not-be-an-amiga-anymore/)

**Zdroj:** 📰 Hackaday
