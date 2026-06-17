---
slug: "igs"
url: "/mobilnisite/slovnik/igs/"
type: "slovnik"
title: "IGS – International GNSS Service"
date: 2025-01-01
abbr: "IGS"
fullName: "International GNSS Service"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/igs/"
summary: "Celosvětová spolupráce více než 200 agentur, která poskytuje vysoce přesná data a produkty ze systémů globální družicové navigace (GNSS). V 3GPP se data IGS používají jako vysoce přesná reference pro"
---

IGS je celosvětová spolupráce poskytující vysoce přesná data GNSS, která 3GPP používá jako přesný referenční rámec pro testování a validaci polohování uživatelských zařízení, aby bylo zajištěno standardizované výkonnostní chování.

## Popis

International [GNSS](/mobilnisite/slovnik/gnss/) Service (IGS) není interní technologie 3GPP, ale externí služba reálného světa, jejíž datové produkty jsou klíčové pro 3GPP certifikační testování polohovacích funkcí. IGS je dobrovolné sdružení více než 200 celosvětových agentur, které sdružují zdroje a data z permanentních stanic GNSS za účelem generování dat a produktů nejvyšší kvality pro komunitu GNSS. Mezi tyto produkty patří přesné efemeridy (dráhy) družic, korekce družicových hodin, parametry rotace Země a globální ionosférické a troposférické modely.

V rámci ekosystému 3GPP je role IGS definována v testovacích specifikacích, zejména pro asistovaný GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Při testování polohovacích schopností UE je vytvořen simulovaný nebo reálný scénář GNSS. „Skutečná“ nebo referenční poloha družic a teoretické podmínky šíření signálu musí být známy s extrémní přesností, aby bylo možné vypočítat očekávaná měření pseudovzdálenosti a následně očekávané určení polohy UE. Právě tuto referenci zlatého standardu poskytují přesná orbitální a časová data IGS. Testovací systémy tato data používají ke generování simulovaných GNSS signálů, které testovaná UE přijímá, nebo k výpočtu očekávaných výsledků z testů se skutečnými signály.

Architektura zahrnuje datová a analytická centra IGS, která zpracovávají data z globální sítě referenčních stanic. Tyto zpracované produkty jsou veřejně dostupné s různým zpožděním (rapidní, finální atd.). Zařízení a simulátory pro 3GPP testování obsahují software, který tyto datové produkty IGS stahuje a využívá. Například v testovacím případě validujícího výkon UE s asistovaným GNSS použije testovací systém přesná efemeridová data IGS k přesnému modelování poloh družic. Následně porovná polohu vypočtenou UE pomocí přijatých asistovaných dat a družicových signálů s „skutečnou“ polohou odvozenou z IGS reference. Tím je zajištěno, že implementace v UE splňuje přísné požadavky na přesnost stanovené ve standardech 3GPP pro nouzové služby, služby založené na poloze a další aplikace.

## K čemu slouží

IGS je ve specifikacích 3GPP referencován, aby poskytoval jednoznačný, vysoce přesný externí referenční rámec pro validaci výkonu polohování. Před rozšířeným přijetím standardizovaných vysoce přesných referencí mohlo testování schopností [GNSS](/mobilnisite/slovnik/gnss/) v UE přinášet nekonzistentní výsledky, protože různé testovací laboratoře mohly používat různé zdroje dat o družicových drahách a hodinách, které se lišily přesností. To ztěžovalo objektivní ověření, zda UE splňuje povinné výkonnostní standardy pro přesnost určení polohy.

Integrace IGS do testovacích specifikací 3GPP řeší problém reprodukovatelnosti testů a srovnávání přesnosti. Stanovuje společnou, celosvětově uznávanou „skutečnou pravdu“, kterou mohou používat všechny strany – výrobci čipových sad, výrobci UE a testovací laboratoře. Toto bylo motivováno regulatorními požadavky na lokalizaci nouzových volajících (např. E911 v USA, eCall v Evropě) a komerční potřebou spolehlivých služeb založených na poloze. Použití dat IGS zajišťuje, že 3GPP testy polohování jsou důkladné, opakovatelné a založené na nejlepších dostupných vědeckých datech, což následně garantuje, že UE nasazená v sítích poskytuje koncovým uživatelům a síťovým službám spolehlivé a přesné informace o poloze.

## Klíčové vlastnosti

- Poskytuje ultra-přesná globální data o družicových drahách a hodinách
- Nabízí globální modely ionosférického a troposférického zpoždění
- Datové produkty dostupné s různým zpožděním (reálný čas, rapidní, finální)
- Slouží jako definitivní reference pro simulaci GNSS signálů při testování
- Umožňuje reprodukovatelné a přesné certifikační testování polohování pro 3GPP
- Podporována globální sítí permanentních GNSS sledovacích stanic

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)

## Definující specifikace

- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [IGS na 3GPP Explorer](https://3gpp-explorer.com/glossary/igs/)
