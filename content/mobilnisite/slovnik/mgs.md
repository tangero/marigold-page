---
slug: "mgs"
url: "/mobilnisite/slovnik/mgs/"
type: "slovnik"
title: "MGS – Medium Grain Scalability"
date: 2025-01-01
abbr: "MGS"
fullName: "Medium Grain Scalability"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mgs/"
summary: "Technika škálovatelnosti při kódování videa definovaná v rozšíření SVC (Scalable Video Coding) standardu H.264/AVC. Umožňuje dekódovat video na různých úrovních kvality selektivním odstraněním skupin"
---

MGS je technika škálovatelnosti při kódování videa v SVC, která umožňuje dekódovat datový proud na různých úrovních kvality selektivním odstraněním skupin transformačních koeficientů.

## Popis

Medium Grain Scalability (MGS) je specifická metoda pro dosažení škálovatelnosti kvality v rámci frameworku Scalable Video Coding (SVC), což je rozšíření standardu pro kompresi videa H.264/[AVC](/mobilnisite/slovnik/avc/). Ve škálovatelném kódování videa obsahuje jeden zakódovaný bitový proud základní vrstvu a jednu či více vylepšujících vrstev. Základní vrstva poskytuje reprezentaci s nejnižší kvalitou a vylepšující vrstvy postupně zvyšují kvalitu, rozlišení (prostorové) nebo snímkovou frekvenci (časové). MGS funguje v oblasti škálovatelnosti kvality (SNR).

Technicky MGS funguje tak, že rozděluje data transformačních koeficientů snímků vylepšující vrstvy do více jednotek [NAL](/mobilnisite/slovnik/nal/) (Network Abstraction Layer). Tyto jednotky NAL, často odpovídající konkrétním frekvenčním pásmům nebo úrovním priority, mohou být selektivně odstraněny prvkem sítě s povědomím o médiu (jako je RAN nebo video optimalizátor) nebo klientem na základě dostupné šířky pásma. Na rozdíl od Fine Grain Scalability (FGS), která umožňuje zkrácení na velmi jemné úrovni bitů, MGS pracuje s hrubšími "kousky" dat – typicky na úrovni granularity jednotek NAL. To představuje praktický střední přístup, který nabízí větší flexibilitu než hrubá [CGS](/mobilnisite/slovnik/cgs/) (Coarse Grain Scalability), kde musí být celé vylepšující vrstvy zachovány nebo zahozeny, ale s nižší složitostí a lepší efektivitou kódování než FGS.

V kontextu 3GPP je MGS specifikováno pro použití v multimediálních vysílacích/multicastových službách (eMBMS) a adaptivním [HTTP](/mobilnisite/slovnik/http/) streamingu (např. [DASH](/mobilnisite/slovnik/dash/)). Síť může přizpůsobit kvalitu videa doručovanou uživateli nebo skupině uživatelů dynamickým přidáváním nebo odebíráním těchto jednotek NAL MGS z přenášeného datového proudu na základě aktuálních rádiových podmínek a přetížení. To umožňuje plynulé přechody kvality bez nutnosti, aby klient přepínal mezi zcela odlišnými předem zakódovanými video soubory, což snižuje nároky na úložiště na serverech a poskytuje plynulejší uživatelský zážitek při kolísání šířky pásma. Specifikace podrobně popisuje, jak jsou vrstvy MGS strukturovány, signalizovány a zpracovávány, aby byla zajištěna interoperabilita mezi kodéry, síťovými prvky a dekodéry.

## K čemu slouží

MGS bylo vyvinuto pro řešení potřeby efektivního a flexibilního přizpůsobování kvality videa v náchylných k chybám a v sítích s proměnlivou šířkou pásma, jako jsou mobilní sítě. Před škálovatelným kódováním vyžadovalo přizpůsobení ukládání více nezávislých kopií (reprezentací) stejného videa na různých datových tocích, což bylo neefektivní z hlediska úložiště a mohlo při přepínání mezi nimi způsobit znatelné skoky v kvalitě (a buffering). Framework SVC a v něm MGS si kladly za cíl vytvořit jediný, vrstvený bitový proud, který by se dal snadno přizpůsobit.

Motivací pro MGS konkrétně bylo najít lepší kompromis. [CGS](/mobilnisite/slovnik/cgs/) bylo jednoduché, ale příliš rigidní, protože vyžadovalo zahození celých vylepšujících vrstev, což vedlo k velkým krokům v kvalitě. FGS bylo extrémně flexibilní, ale trpělo výraznou ztrátou efektivity kódování (vyšší datový tok při stejné kvalitě) a vysokou výpočetní složitostí. MGS bylo zavedeno jako kompromis, poskytující více mezilehlých kroků kvality (více než CGS) při zachování efektivity kódování mnohem blíže efektivitě jednovrstvového (neskalovatelného) kódování. To z něj učinilo technicky a ekonomicky životaschopnou volbu pro mobilní streamování a vysílací služby, kde jsou síťové podmínky dynamické a heterogenní napříč uživateli.

## Klíčové vlastnosti

- Poskytuje škálovatelnost kvality (SNR) v rámci standardu H.264/SVC
- Rozděluje data vylepšující vrstvy na selektivně odstranitelné jednotky NAL
- Nabízí granularitu mezi hrubozrnnou (CGS) a jemnozrnnou škálovatelností (FGS)
- Umožňuje přizpůsobení bitového proudu na straně sítě nebo klienta bez nutnosti plné transkódace
- Zlepšuje efektivitu kódování ve srovnání s FGS při zachování flexibility přizpůsobení
- Specifikováno pro použití ve službách 3GPP eMBMS a adaptivního streamování

## Související pojmy

- [CGS – Coarse Grain Scalability](/mobilnisite/slovnik/cgs/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS

---

📖 **Anglický originál a plná specifikace:** [MGS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mgs/)
