---
slug: "pdc-efr"
url: "/mobilnisite/slovnik/pdc-efr/"
type: "slovnik"
title: "PDC-EFR – Personal Digital Cellular - Enhanced Full Rate"
date: 2025-01-01
abbr: "PDC-EFR"
fullName: "Personal Digital Cellular - Enhanced Full Rate"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/pdc-efr/"
summary: "Řečový kodek s přenosovou rychlostí 6,7 kbit/s standardizovaný sdružením ARIB pro japonský systém PDC a později přijatý 3GPP. Poskytuje vylepšenou kvalitu hlasu pro sítě 2G digitální buňkové komunikac"
---

PDC-EFR je řečový kodek s přenosovou rychlostí 6,7 kbit/s standardizovaný pro japonský systém PDC a později přijatý 3GPP za účelem poskytnutí vylepšené kvality hlasu pro sítě 2G digitální buňkové komunikace.

## Popis

PDC-EFR (Personal Digital Cellular - Enhanced Full Rate) je algoritmus kódování řeči pracující s přenosovou rychlostí 6,7 kilobitů za sekundu. Původně jej vyvinulo sdružení [ARIB](/mobilnisite/slovnik/arib/) (Association of Radio Industries and Businesses) pro japonský 2G systém Personal Digital Cellular. Technicky se jedná o kodek založený na metodě [CELP](/mobilnisite/slovnik/celp/) (code-excited linear prediction), navržený tak, aby poskytoval lepší kvalitu řeči než předchozí kodek PDC-FR ([PDC](/mobilnisite/slovnik/pdc/) Full Rate), který pracoval na podobné přenosové rychlosti, ale s nižší percepční kvalitou. Konstrukce kodeku se zaměřuje na rovnováhu mezi kompresní účinností a přirozeností a srozumitelností řeči, což jej činí vhodným pro rádiové kanály s omezenou šířkou pásma v systémech buňkové komunikace založených na [TDMA](/mobilnisite/slovnik/tdma/).

V rámci architektury 3GPP je PDC-EFR specifikován jako přenosový kodek pro doménu přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)), především pro scénáře interoperability se staršími systémy a roaming. Je definován ve specifikaci 3GPP TS 26.093, která podrobně popisuje algoritmické detaily, testovací sekvence a požadavky na shodu. Kodek funguje tak, že analyzuje krátké segmenty (rámce) řečového vstupu, extrahuje parametry lineární prediktivní kódování ([LPC](/mobilnisite/slovnik/lpc/)) a pro modelování excitačního signálu používá adaptivní kodebook a pevný kodebook. Tato parametrická reprezentace je následně přenášena přes rozhraní vzduchu, kde přijímač syntetizuje řečový signál pomocí přijatých parametrů.

Jeho úlohou v síti je být jednou z možností konkrétního hlasového kodeku v rámci funkce adaptace terminálu ([TAF](/mobilnisite/slovnik/taf/)) a jednotky transkódování a adaptace přenosové rychlosti ([TRAU](/mobilnisite/slovnik/trau/)). Když mobilní stanice podporující PDC-EFR naváže hlasové volání, procedury vyjednávání kodeku určí, zda lze PDC-EFR použít end-to-end, nebo zda je v jádrové síti vyžadováno transkódování na jiný kodek (např. AMR). Ačkoli byl tento kodek z velké části nahrazen vlastní rodinou kodeků 3GPP Adaptive Multi-Rate (AMR) v sítích UMTS a LTE, PDC-EFR zůstává definovanou součástí pro zajištění zpětné kompatibility a podporu specifických regionálních nasazení, zejména těch zahrnujících starší infrastrukturu japonské sítě PDC.

## K čemu slouží

Kodek PDC-EFR byl vytvořen, aby řešil potřebu vyšší kvality hlasových služeb v rámci omezeného rádiového spektra přiděleného japonskému 2G systému PDC. Původní kodek PDC-FR byl sice spektrálně účinný, ale měl omezení v percepční kvalitě, která se stala patrná s rostoucími očekáváními uživatelů. Motivací bylo vyvinout vylepšený kodek, který by mohl pracovat ve stejné základní struktuře kanálu (např. kapacita časového slotu), ale poskytovat kvalitu řeči srovnatelnou nebo lepší než jiné současné standardy digitální buňkové komunikace, čímž by se zlepšila spokojenost zákazníků a konkurenceschopnost.

Historicky byl jeho vývoj součástí vývoje japonského trhu digitální buňkové komunikace v 90. letech 20. století. Přijetím pokročilých technik CELP chtělo sdružení ARIB maximalizovat využitelnost nasazené infrastruktury TDMA bez nutnosti změn hardwaru základní šířky pásma kanálu nebo časování slotů. Kodek vyřešil problém vnímané 'kovovosti' nebo umělosti hlasu spojené s dřívějšími vokodéry a poskytl přirozenější a robustnější řečový zážitek, zejména v hlučném prostředí.

Jeho začlenění do specifikací 3GPP, počínaje Release 8, bylo motivováno potřebou globální standardizace pro zajištění roamingu a interoperability. Jak se systémy 3GPP rozšiřovaly, začaly zahrnovat podporu různých regionálních kodeků, aby bylo zajištěno, že více režimová zařízení mohou bezproblémově fungovat napříč různými staršími sítěmi. Standardizace PDC-EFR poskytuje jasný referenční rámec pro implementaci a testování, což zajišťuje, že sítě a zařízení dokážou zpracovat hovory pocházející z regionů nebo směřující do regionů, kde byl tento kodek historicky nasazen, a tím řeší problém kontinuity služeb a kvality pro roamující účastníky.

## Klíčové vlastnosti

- Provoz s pevnou přenosovou rychlostí 6,7 kbit/s
- Algoritmus CELP (Code-Excited Linear Prediction)
- Vylepšená kvalita řeči oproti předchůdci PDC-FR
- Zpracování na bázi rámců pro efektivní přenos
- Standardizované testovací vektory pro ověření shody
- Definován pro interoperabilitu v doméně přepojování okruhů (CS) 3GPP

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [TRAU – Transcoder and Rate Adaptation Unit (Frame)](/mobilnisite/slovnik/trau/)
- [ARIB – Association of Radio Industries and Businesses](/mobilnisite/slovnik/arib/)

## Definující specifikace

- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS

---

📖 **Anglický originál a plná specifikace:** [PDC-EFR na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdc-efr/)
