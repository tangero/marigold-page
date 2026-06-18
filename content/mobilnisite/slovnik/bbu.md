---
slug: "bbu"
url: "/mobilnisite/slovnik/bbu/"
type: "slovnik"
title: "BBU – Base Band Unit"
date: 2025-01-01
abbr: "BBU"
fullName: "Base Band Unit"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bbu/"
summary: "Jednotka základního pásma (BBU) je klíčovou komponentou architektury mobilní sítě, která zpracovává signály základního pásma. Zajišťuje funkce digitálního zpracování signálu, jako je kanálové kódování"
---

BBU je jednotka pro zpracování základního pásma v mobilní síti, která zajišťuje funkce digitálního zpracování signálu, jako je kanálové kódování a modulace, a odděluje je od vysokofrekvenčních funkcí, čímž umožňuje flexibilní nasazení.

## Popis

Jednotka základního pásma (BBU) je základní komponentou moderních architektur mobilních sítí, zejména v distribuovaných nasazeních rádiové přístupové sítě (RAN). Slouží jako uzel pro digitální zpracování signálu, který zajišťuje veškeré operace základního pásma před převodem signálů na vysokofrekvenční. BBU plní kritické funkce včetně kanálového kódování a dekódování, modulace a demodulace, digitálního formování svazku, plánovacích algoritmů a správy rozhraní s jádrem sítě. Pracuje s digitalizovanými signály a implementuje protokoly fyzické vrstvy a části protokolů [MAC](/mobilnisite/slovnik/mac/) vrstvy podle specifikací 3GPP.

Architektonicky je BBU typicky nasazována na centralizovaném místě, často v tzv. hotelu základnových stanic nebo datovém centru, kde může být více BBU sdruženo do poolu. Toto centralizované nasazení umožňuje sdílení zdrojů, snazší údržbu a snížení provozních nákladů. BBU je připojena ke vzdáleným rádiovým hlavám ([RRH](/mobilnisite/slovnik/rrh/)) prostřednictvím vysokokapacitních, nízkolatenčních rozhraní pro propojení s přístupovou částí (fronthaul), nejčastěji s využitím protokolů Common Public Radio Interface (CPRI) nebo enhanced CPRI (eCPRI). Toto oddělení zpracování základního pásma od rádiového přenosu umožňuje flexibilní topologie sítě a efektivní využití zdrojů.

Vnitřní architektura BBU se skládá z několika klíčových komponent: digitálních signálových procesorů ([DSP](/mobilnisite/slovnik/dsp/)) pro zpracování fyzické vrstvy, procesorů pro všeobecné použití pro vyšší protokolové vrstvy, paměťových podsystémů pro vyrovnávací paměť a úložiště a rozhraní pro připojení k sítím pro propojení s přístupovou částí (fronthaul) i pro propojení s přenosovou sítí (backhaul). Implementuje sofistikované algoritmy pro správu interference, řízení výkonu a vynucování kvality služeb (QoS). BBU také zajišťuje funkce správy mobility, jako je příprava a provedení předání spojení, což je klíčové pro udržení nepřerušovaného připojení při pohybu uživatelů v síti.

V sítích 5G se koncept BBU vyvinul do architektury rozdělené na centralizovanou jednotku ([CU](/mobilnisite/slovnik/cu/)) a distribuovanou jednotku ([DU](/mobilnisite/slovnik/du/)), kde jsou tradiční funkce BBU rozděleny mezi tyto dvě logické entity. Základní princip oddělení zpracování základního pásma od rádiového přenosu však zůstává. Role BBU ve virtualizaci sítě je obzvláště významná, protože umožňuje architektury cloudového RAN (C-RAN), kde mohou být funkce zpracování základního pásma virtualizovány a provozovány na hardware pro všeobecné použití v datových centrech.

Zpracovatelské schopnosti BBU přímo ovlivňují metriky výkonu sítě včetně propustnosti, latence a hustoty připojení. Implementuje pokročilé funkce jako agregaci nosných, zpracování více vstupů/více výstupů ([MIMO](/mobilnisite/slovnik/mimo/)) a algoritmy pro potlačení interference. BBU také hraje klíčovou roli v energetické účinnosti sítě prostřednictvím inteligentních algoritmů řízení výkonu, které mohou dynamicky škálovat zpracovatelské zdroje na základě vytížení přenosové sítě, což přispívá k udržitelnějšímu provozu sítě.

## K čemu slouží

BBU byla vyvinuta k řešení několika omezení tradičních architektur integrovaných základnových stanic, kde byly vysokofrekvenční funkce a zpracování základního pásma kombinovány v jedné jednotce. V konvenčních základnových stanicích byly obě funkce umístěny společně na místě buňky, což vedlo k neefektivnímu využití prostoru, energie a chladicích zdrojů. Tato architektura také ztěžovala modernizaci a údržbu sítě, protože technici museli pro jakékoli změny hardwaru nebo softwaru navštívit každé místo buňky. Oddělení zpracování základního pásma do BBU umožnilo flexibilnější a nákladově efektivnější nasazení sítí.

Hlavní motivací pro vývoj BBU bylo umožnit centralizované architektury RAN, kde může být více jednotek pro zpracování základního pásma sdruženo na centralizovaných místech. Tato centralizace umožňuje zisky ze statistického multiplexování, kdy mohou být zpracovatelské zdroje dynamicky přidělovány mezi více míst buněk na základě charakteru provozu. Také usnadňuje implementaci pokročilých funkcí, jako je koordinovaný vícebodový přenos a příjem (CoMP), který vyžaduje těsnou koordinaci mezi více buňkami. Architektura s oddělením BBU a [RRH](/mobilnisite/slovnik/rrh/) snižuje provozní náklady zjednodušením požadavků na místo buňky a umožněním efektivnějšího využití prostoru.

Dalším klíčovým účelem architektury BBU je podpora virtualizace sítě a cloudových implementací. Oddělením funkce zpracování základního pásma mohou operátoři nasazovat BBU na běžně dostupném hardwaru ([COTS](/mobilnisite/slovnik/cots/)) v datových centrech a vzdalovat se od proprietárních hardwarových řešení. To umožňuje agilnější nasazení a škálování sítě, stejně jako snazší integraci s technologiemi virtualizace síťových funkcí (NFV) a softwarově definovaných sítí (SDN). Architektura BBU také podporuje vývoj směrem k otevřeným rozhraním RAN, což podporuje interoperabilitu více dodavatelů a inovace v rádiové přístupové síti.

## Klíčové vlastnosti

- Digitální zpracování signálu pro funkce fyzické vrstvy
- Správa rozhraní pro propojení s přístupovou částí (CPRI/eCPRI) a připojení k přenosové síti
- Plánovací algoritmy pro přidělování rádiových zdrojů
- Podpora více anténních technologií včetně MIMO
- Schopnosti agregace nosných
- Podpora virtualizace pro nasazení cloudového RAN

## Definující specifikace

- **TS 22.864** (Rel-15) — 5G Network Operation Use Cases & Requirements
- **TR 38.913** (Rel-19) — Next Gen Access Tech Scenarios & Requirements
- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study

---

📖 **Anglický originál a plná specifikace:** [BBU na 3GPP Explorer](https://3gpp-explorer.com/glossary/bbu/)
