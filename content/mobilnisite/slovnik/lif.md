---
slug: "lif"
url: "/mobilnisite/slovnik/lif/"
type: "slovnik"
title: "LIF – Location Interoperability Forum"
date: 2025-01-01
abbr: "LIF"
fullName: "Location Interoperability Forum"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lif/"
summary: "Fórum v rámci 3GPP odpovědné za definování standardizovaných lokalizačních služeb a rozhraní. Zajišťuje interoperabilitu mezi síťovými prvky a poskytovateli lokalizačních služeb, což umožňuje konziste"
---

LIF je fórum v rámci 3GPP odpovědné za definování standardizovaných lokalizačních služeb a rozhraní, které zajišťuje interoperabilitu mezi síťovými prvky a poskytovateli lokalizačních služeb.

## Popis

Location Interoperability Forum (LIF) je standardizační orgán, který byl původně založen mimo 3GPP, ale jehož specifikace byly později přijaty a jsou udržovány v rámci 3GPP, primárně v pracovní skupině TSG SA WG1 (Services). Jeho hlavním zaměřením je vývoj a údržba technických specifikací pro mobilní lokalizační služby ([LCS](/mobilnisite/slovnik/lcs/)), se silným důrazem na vytváření otevřených, interoperabilních rozhraní mezi mobilní sítí a aplikacemi lokalizačních služeb. Jádro architektury definované LIF se točí kolem Mobile Location Protocol ([MLP](/mobilnisite/slovnik/mlp/)), což je aplikační protokol pro dotazování na polohu mobilních stanic. MLP používá XML přes [HTTP](/mobilnisite/slovnik/http/)/S a definuje standardní servisní elementy, jako je Standard Location Immediate Request a Emergency Location Immediate Request. Klíčovými komponentami v architektuře LIF jsou Location Server (který hostuje LCS klienta) a Gateway Mobile Location Center ([GMLC](/mobilnisite/slovnik/gmlc/)) v síti, přičemž MLP slouží jako klíčové rozhraní mezi nimi. Toto oddělení umožňuje vývojářům aplikací žádat o lokalizační informace bez nutnosti hluboké znalosti podkladové rádiové přístupové technologie (např. GSM, UMTS, LTE). Práce fóra zajišťuje, že služby jako lokalizace volajícího v nouzových případech (E911/E112), sledování vozového parku nebo aplikace pro vyhledání přátel mohou být nasazeny konzistentně, bez ohledu na dodavatele sítě nebo operátora, a to poskytnutím jasné, bezpečné a škálovatelné servisní vrstvy pro získávání lokalizačních informací.

## K čemu slouží

LIF byl vytvořen k řešení kritického problému fragmentace na raném trhu mobilních lokalizačních služeb. Před jeho založením používali dodavatelé síťového vybavení a vývojáři aplikací proprietární, neinteroperabilní rozhraní pro přístup k lokalizačním datům z mobilních sítí. To ztěžovalo a prodražovalo nasazení aplikací založených na poloze napříč více operátory nebo v různých zemích, což vážně omezovalo růst trhu a inovace. Hlavní motivací fóra bylo umožnit masové lokalizační služby definováním jediného, otevřeného standardu – Mobile Location Protocol ([MLP](/mobilnisite/slovnik/mlp/)) – který může být implementován libovolným síťovým operátorem a používán libovolným poskytovatelem aplikací. Klíčovým hybatelem byly také regulatorní požadavky, zejména potřeba standardizovaných nouzových služeb (E911 v USA, E112 v Evropě), které vyžadovaly přesné, na síti nezávislé hlášení polohy. Poskytnutím společné technické základny LIF řešil omezení plynoucí z uzamčení u jednoho dodavatele a umožnil ekosystém, ve kterém mohou vývojáři třetích stran vytvářet inovativní služby založené na poloze ([LBS](/mobilnisite/slovnik/lbs/)), které budou bezproblémově fungovat na jakékoli kompatibilní síti, čímž se celosvětově urychlila adopce LBS.

## Klíčové vlastnosti

- Standardizuje Mobile Location Protocol (MLP) pro lokalizační požadavky a odpovědi
- Definuje XML-based servisní elementy pro okamžité, odložené a nouzové lokalizační dotazy
- Specifikuje bezpečné transportní mechanismy využívající HTTPS pro ochranu soukromí a integritu
- Podporuje více formátů polohy včetně adresních údajů a zeměpisných souřadnic
- Umožňuje interoperabilitu mezi síťovými operátory a poskytovateli lokalizačních služeb třetích stran
- Usnadňuje splnění regulatorních požadavků pro lokalizaci v nouzových službách (E911/E112)

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [MLP – Mobile Location Protocol](/mobilnisite/slovnik/mlp/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)

## Definující specifikace

- **TR 21.902** (Rel-10) — 3GPP Evolution Roadmap
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture

---

📖 **Anglický originál a plná specifikace:** [LIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lif/)
