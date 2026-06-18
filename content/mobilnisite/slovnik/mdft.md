---
slug: "mdft"
url: "/mobilnisite/slovnik/mdft/"
type: "slovnik"
title: "MDFT – Modified Discrete Fourier Transform"
date: 2025-01-01
abbr: "MDFT"
fullName: "Modified Discrete Fourier Transform"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mdft/"
summary: "Transformace používaná ve zpracování signálů v 5G NR, zejména pro referenční signály jako jsou Demodulační referenční signály (DM-RS). Modifikuje standardní DFT za účelem optimalizace výkonu pro speci"
---

MDFT je modifikovaná diskrétní Fourierova transformace používaná v 5G NR k optimalizaci výkonu referenčních signálů pro specifické délky sekvencí a generování vlnových forem s nízkým PAPR.

## Popis

Modifikovaná diskrétní Fourierova transformace (MDFT) je specializovaná matematická transformace používaná ve fyzické vrstvě 5G New Radio (NR). Jedná se o variantu standardní diskrétní Fourierovy transformace ([DFT](/mobilnisite/slovnik/dft/)), která je optimalizována pro generování sekvencí se specifickými vlastnostmi klíčovými pro moderní bezdrátovou komunikaci. Jejím hlavním uplatněním v 3GPP je generování Demodulačních referenčních signálů ([DM-RS](/mobilnisite/slovnik/dm-rs/)) v uplinku, zejména při použití vlnové formy DFT-s-OFDM (Discrete Fourier Transform Spread Orthogonal Frequency Division [Multiplexing](/mobilnisite/slovnik/multiplexing/)), což je v 5G ekvivalent [SC-FDMA](/mobilnisite/slovnik/sc-fdma/) používaného v LTE uplinku. MDFT je definována tak, aby vytvářela sekvence referenčních signálů s nízkým poměrem špičkového a průměrného výkonu ([PAPR](/mobilnisite/slovnik/papr/)) a dobrými korelačními vlastnostmi.

Technicky MDFT pracuje se vstupní sekvencí délky M (často základní sekvencí, jako je Zadoff-Chuova sekvence nebo počítačově generovaná sekvence) a transformuje ji na výstupní sekvenci délky N, kde M a N jsou specifická celá čísla definovaná standardem, a typicky je M menší nebo rovno N. Modifikace spočívá v konkrétním indexování a fázových faktorech aplikovaných během transformace. Standardní vzorec DFT je upraven tak, aby výsledné symboly ve frekvenční oblasti, při mapování na specifické subnosné a převodu do časové oblasti prostřednictvím inverzní DFT ([IDFT](/mobilnisite/slovnik/idft/)) jako součásti procesu DFT-s-OFDM, dávaly časový signál s žádoucími vlastnostmi. Klíčová modifikace často zahrnuje cyklický posuv nebo specifickou fázovou rotaci v definici transformace, aby byla sekvence optimálně zarovnána v rámci přidělených zdrojových bloků.

Jak to funguje v praxi: Pro generování DM-RS je definována základní sekvence. Na tuto základní sekvenci je aplikována MDFT za účelem vytvoření sekvence referenčního signálu ve frekvenční oblasti. Tato sekvence je následně namapována na určené zdrojové elementy (subnosné) DM-RS v rámci [OFDM](/mobilnisite/slovnik/ofdm/) symbolu. Charakteristika nízkého PAPR je pro uplink kritická, protože umožňuje výkonovému zesilovači uživatelského zařízení (UE) pracovat efektivněji, čímž prodlužuje výdrž baterie a zvyšuje pokrytí. Konstrukce MDFT zajišťuje, že i pro různé délky sekvencí a přidělení zdrojů si generovaný DM-RS zachovává konzistentní a optimální výkon. Jeho role je zabudována do procesu odhadu kanálu na gNodeB, kde je přijatý DM-RS, transformovaný inverzním procesem, použit k odhadu rádiového kanálu pro přesnou demodulaci dat.

## K čemu slouží

MDFT byla zavedena, aby řešila specifické výzvy v návrhu vlnové formy pro 5G NR uplink. Primárním účelem je generovat sekvence referenčních signálů (konkrétně pro [DM-RS](/mobilnisite/slovnik/dm-rs/)), které mají velmi nízký poměr špičkového a průměrného výkonu (PAPR) při použití s vlnovou formou DFT-s-OFDM. Nízký PAPR je prvořadým požadavkem pro uplinkové přenosy z mobilních zařízení, protože vysoký PAPR nutí výkonový zesilovač pracovat neefektivně ve své nelineární oblasti, což vede k vyšší spotřebě energie, snížené výdrži baterie a nežádoucím emisím mimo pásmo. Standardní DFT, když je aplikována přímo na některé sekvence, negarantuje nejnižší možný PAPR pro všechny délky sekvencí a přidělení zdrojů.

Historicky LTE používalo pro uplinkové referenční signály jiné mechanismy. S flexibilnější numerologií 5G (proměnná vzdálenost subnosných) a širším rozsahem podporovaných šířek pásem byl zapotřebí obecnější a optimalizovanější přístup. MDFT tuto optimalizaci poskytuje. Řeší problém efektivního generování velké sady sekvencí referenčních signálů (pro podporu mnoha uživatelů a vrstev), které si všechny zachovávají vynikající charakteristiky PAPR. To byl klíčový motiv pro její vytvoření v Release 18, jelikož vylepšení výkonu a efektivity uplinku bylo jednou z hlavních oblastí zájmu.

Dále MDFT umožňuje lepší výkon ve scénářích s vysokou mobilitou a pro pokročilé víceanténní techniky (MIMO). Tím, že poskytuje referenční signály s dobrými vlastnostmi autokorelace a vzájemné korelace, je zlepšena přesnost odhadu kanálu, což je klíčové pro dosažení vysokých přenosových rychlostí a cílů spolehlivosti 5G-Advanced. Její specifikace v TS 26.253 (původně pro jiné účely) a přijetí pro signály fyzické vrstvy ilustruje mezivrstvovou optimalizaci v 3GPP, kde jsou matematické nástroje pečlivě vybírány, aby splnily přísné systémové požadavky na energetickou účinnost, kvalitu signálu a flexibilitu implementace.

## Klíčové vlastnosti

- Optimalizovaná varianta DFT pro generování sekvencí s nízkým PAPR
- Primárně používaná pro generování Demodulačních referenčních signálů (DM-RS) v 5G NR uplinku
- Definována pro specifické délky vstupní (M) a výstupní (N) sekvence dle specifikace 3GPP
- Zvyšuje účinnost výkonového zesilovače v uživatelském zařízení (UE) snížením špiček signálu
- Podporuje vlnovou formu DFT-s-OFDM (SC-FDMA) pro uplinkový přenos
- Zlepšuje přesnost odhadu kanálu díky dobře navrženým vlastnostem sekvencí

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [MDFT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdft/)
