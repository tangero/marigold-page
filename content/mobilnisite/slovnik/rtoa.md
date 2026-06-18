---
slug: "rtoa"
url: "/mobilnisite/slovnik/rtoa/"
type: "slovnik"
title: "RTOA – Relative Time of Arrival"
date: 2025-01-01
abbr: "RTOA"
fullName: "Relative Time of Arrival"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rtoa/"
summary: "RTOA je technika měření polohy používaná v LTE a 5G NR k odhadu polohy uživatelského zařízení (UE) výpočtem relativního časového rozdílu příchodu signálů z více základnových stanic. Je to základní met"
---

RTOA je technika měření polohy, která odhaduje umístění zařízení výpočtem relativního časového rozdílu příchodu signálů z více základnových stanic v sítích LTE a 5G.

## Popis

Relative Time of Arrival (RTOA) je síťová metoda určování polohy standardizovaná 3GPP pro LTE a 5G New Radio (NR). Funguje na principu měření časového rozdílu mezi příchodem rádiových signálů z více geograficky oddělených základnových stanic (eNodeB v LTE, gNB v NR) k cílovému uživatelskému zařízení (UE). UE nebo síť měří Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) pro referenční signály určené k určování polohy ([PRS](/mobilnisite/slovnik/prs/)), které jsou pro tento účel speciálně navrženy. Tyto PRS jsou vysílány s přesným časováním ze synchronizovaných základnových stanic. Základním principem je multilaterace: díky znalosti přesného času vysílání z každé buňky a změřených časů příchodu na UE definují rozdíly těchto časů hyperbolické linie polohy. Průsečík více takových hyperbol určuje polohu UE.

Architektura zahrnuje UE, obsluhující a sousední základnové stanice a polohový server (např. Evolved Serving Mobile Location Centre - [E-SMLC](/mobilnisite/slovnik/e-smlc/) v LTE, Location Management Function - [LMF](/mobilnisite/slovnik/lmf/) v 5G). Polohový server nakonfiguruje UE pomocnými daty, která specifikují konfiguraci PRS (prvky prostředků, vzory utlumení) sousedních buněk. UE následně provádí RTOA měření na těchto PRS a hlásí změřené časové rozdíly (Reference Signal Time Differences - [RSTD](/mobilnisite/slovnik/rstd/)) zpět polohovému serveru. Server, který má k dispozici známé zeměpisné souřadnice a přesné časování všech zúčastněných základnových stanic, vypočítá polohu UE pomocí algoritmů, jako je metoda nejmenších čtverců nebo odhad Taylorovou řadou, k řešení hyperbolických rovnic.

Klíčem k přesnosti RTOA je synchronizace sítě základnových stanic. V LTE je toho obvykle dosaženo pomocí globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)) nebo přesných časových protokolů, jako je [IEEE](/mobilnisite/slovnik/ieee/) 1588v2 ([PTP](/mobilnisite/slovnik/ptp/)). V 5G NR jsou požadavky ještě přísnější, aby podpořily vyšší přesnost. Na výkon techniky mají vliv faktory jako poměr signálu k šumu, vícestopé šíření, podmínky bez přímé viditelnosti a geometrie základnových stanic vůči UE (zředění přesnosti). Pro zmírnění těchto efektů a zlepšení přesnosti určování polohy, zejména uvnitř budov, byly v pozdějších vydáních zavedeny vylepšení, jako jsou měření fáze nosné a podpora širších šířek pásma.

Role RTOA v síti je klíčová pro regulační požadavky, jako je určení polohy volajícího v nouzových případech (E911/E112), komerční služby založené na poloze (LBS) a optimalizaci sítě. Poskytuje doplňkovou nebo alternativní metodu určování polohy k satelitním systémům (GPS, Galileo), které mohou být uvnitř budov nebo v městských kaňonech nedostupné nebo se zhoršeným signálem. Jako součást širší metody určování polohy Observed Time Difference of Arrival (OTDOA) tvoří RTOA základní měření, na kterém je výpočet polohy postaven, což z ní dělá základní kámen terestriálních schopností určování polohy podle 3GPP.

## K čemu slouží

RTOA bylo zavedeno, aby splnilo rostoucí regulační a komerční poptávku po přesném určování polohy mobilních zařízení. Regulační orgány po celém světě nařídily, aby síťoví operátoři poskytovali informace o poloze pro nouzové hovory (např. E911 v USA). Zatímco GNSS poskytuje vynikající přesnost venku, uvnitř budov nebo v hustém městském prostředí je často nedostupné kvůli blokaci signálu. RTOA bylo vyvinuto, aby poskytlo spolehlivé síťové terestriální řešení určování polohy, které nezávisí na tom, zda má UE volný výhled na satelity.

Technologie řeší omezení předchozích metod určování polohy v buňkových sítích, jako je Cell-ID (který nabízí pouze hrubou přesnost na úrovni buňky) a Enhanced Cell-ID (který používá časový předstih a sílu signálu pro o něco lepší přesnost, ale stále je omezený). RTOA využitím multilaterace napříč více základnovými stanicemi poskytuje výrazně vyšší přesnost, potenciálně až na desítky metrů v závislosti na hustotě sítě a kvalitě synchronizace. Jeho vytvoření bylo motivováno potřebou standardizované, škálovatelné a přesné metody, kterou by bylo možné implementovat napříč heterogenními nasazeními sítí, od hustých městských makrobuněk po vnitřní small buňky.

Historicky byl koncept Time Difference of Arrival (TDOA) používán v radaru a dalších rádiových systémech. Standardizace RTOA/OTDOA ze strany 3GPP ve vydání 9 (se základní prací ve vydání 8) přinesla tuto techniku do oblasti buňkových sítí, definovala specifické referenční signály (PRS) a protokoly, aby fungovala v rámci složitého rámce LTE a později 5G NR. Vyřešila problém vytvoření všudypřítomné polohové vrstvy v rámci samotné buňkové infrastruktury, čímž zajistila soulad se zákony o nouzových službách a umožnila novou vlnu aplikací využívajících polohu.

## Klíčové vlastnosti

- Založeno na měřeních Observed Time Difference of Arrival (OTDOA)
- Využívá vyhrazené referenční signály pro určování polohy (PRS) pro vysokou přesnost měření
- Podporuje režimy určování polohy s asistencí UE a režimy založené na UE
- Vyžaduje vysoce synchronizovanou síť základnových stanic (např. pomocí GNSS nebo PTP)
- Výkon vylepšen měřením fáze nosné v pozdějších vydáních
- Škálovatelné napříč nasazeními makro, mikro a piko buněk

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 36.112** (Rel-19) — E-UTRAN LMU Conformance Requirements

---

📖 **Anglický originál a plná specifikace:** [RTOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/rtoa/)
