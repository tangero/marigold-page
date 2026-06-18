---
slug: "tdt"
url: "/mobilnisite/slovnik/tdt/"
type: "slovnik"
title: "TDT – Time and Date Table"
date: 2025-01-01
abbr: "TDT"
fullName: "Time and Date Table"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tdt/"
summary: "Tabulka času a data (TDT) je datová struktura definovaná v 3GPP pro službu Multimedia Broadcast/Multicast Service (MBMS). Poskytuje absolutní časové informace tím, že koreluje společnou časovou osu sí"
---

TDT je datová struktura v 3GPP MBMS, která poskytuje absolutní časové informace korelací časové osy sítě MBMS se světovým časem UTC.

## Popis

Tabulka času a data (TDT) je klíčový synchronizační prvek v architektuře služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) dle 3GPP, specifikovaný v TS 26.917. Jedná se o specifický typ tabulky nebo zprávy, která nese absolutní informace o čase a datu, explicitně mapující společnou časovou osu MBMS – nepřetržitý, v celé síti platný čítač – na koordinovaný světový čas ([UTC](/mobilnisite/slovnik/utc/)). Samotná společná časová osa MBMS je přenášena prostřednictvím tabulky [MCT](/mobilnisite/slovnik/mct/) (Common Timeline), která poskytuje relativní počet tiků. TDT poskytuje zásadní referenční bod tím, že v určitém okamžiku uvádí odpovídající datum a čas UTC.

Z architektonického hlediska je TDT generována a vkládána do transportního proudu MBMS centrem Broadcast Multicast Service Centre ([BM-SC](/mobilnisite/slovnik/bm-sc/)). Následně je distribuována přes síť přenosové cesty MBMS ke všem základnovým stanicím evolved NodeB ([eNB](/mobilnisite/slovnik/enb/)) ve vysílací oblasti. TDT funguje ve spojení se synchronizačním mechanismem čísla systémového rámce ([SFN](/mobilnisite/slovnik/sfn/)) v rádiové přístupové síti. Přijetím TDT mohou koncová zařízení (UE) provádět dvě klíčové funkce: za prvé mohou synchronizovat své vnitřní hodiny s UTC s vysokou přesností; za druhé, a to je důležitější, mohou vypočítat přesný čas UTC pro jakoukoli budoucí událost naplánovanou na společné časové ose MBMS. To umožňuje zařízením UE probouzet se z klidového nebo spánkového režimu přesně ve správný okamžik pro příjem naplánovaného obsahu, čímž se šetří životnost baterie.

Její role je zásadní pro doručování služeb založených na čase v MBMS a evolved MBMS (eMBMS). Služby jako File Delivery over Unidirectional Transport ([FLUTE](/mobilnisite/slovnik/flute/)) pro stahování souborů, elektronické průvodce službami ([ESG](/mobilnisite/slovnik/esg/)) a naplánované vysílací relace jsou na synchronizaci pomocí TDT závislé. Například oznámení služby může zařízení UE sdělit, že cenná softwarová aktualizace bude vysílána při hodnotě X na společné časové ose. Bez TDT zařízení zná pouze relativní tik. S TDT může zařízení převést tik X na absolutní datum a čas UTC, podle toho naplánovat svůj přijímač a zajistit, že bude aktivní pro zachycení přenosu. To umožňuje efektivní, sítí řízené a šetrné hromadné rozesílání obsahu, které nevyčerpává baterii.

## K čemu slouží

TDT byla vytvořena k řešení problému synchronizace v asynchronních vysílacích/multicastových sítích. V bodové (point-to-point) mobilní síti lze časování spravovat přímou signalizací s každým zařízením UE. Ve vysílacím scénáři, kde jeden přenos cílí na potenciálně miliony zařízení, byl potřeba efektivní společný způsob pro zarovnání všech přijímačů na univerzální plán. Předchozí přístupy postrádaly standardizovaný způsob korelace interního plánu doručování sítě se světovým časem.

Její zavedení, zejména s vylepšeními eMBMS, bylo motivováno potřebou podporovat služby plánovaného doručování obsahu, jako je mobilní TV, distribuce velkých souborů (např. pro automobilové softwarové aktualizace) a systémy veřejného varování. Tyto služby vyžadují, aby zařízení přesně věděla, *kdy* mají naslouchat, nejen *co* mají poslouchat. TDT řeší omezení pouhé relativní časové osy (MCT) tím, že poskytuje absolutní časový referenční bod. To umožňuje funkce šetřící energii (nespojitý příjem zarovnaný s plány obsahu) a spolehlivou aktivaci služeb, což je klíčové jak pro spotřebitelské vysílací služby, tak pro aplikace IoT s kritickým nasazením. Poskytuje časový základ, díky kterému jsou plánované služby MBMS praktické a efektivní.

## Klíčové vlastnosti

- Poskytuje korelaci absolutního času a data UTC pro společnou časovou osu MBMS
- Nezbytná pro synchronizaci přijímačů UE s naplánovanými vysílacími/multicastovými relacemi
- Umožňuje úsporu energie prostřednictvím přesného plánování probuzení pro příjem obsahu
- Generována a distribuována centrem BM-SC napříč sítí MBMS
- Funguje ve spojení s tabulkou MCT (Common Timeline)
- Základní pro fungování doručování souborů FLUTE a elektronického průvodce službami (ESG)

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MCT – Multi-channel Coding Tool](/mobilnisite/slovnik/mct/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [TDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdt/)
