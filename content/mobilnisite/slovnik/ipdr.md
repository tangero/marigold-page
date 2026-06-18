---
slug: "ipdr"
url: "/mobilnisite/slovnik/ipdr/"
type: "slovnik"
title: "IPDR – Internet Protocol Detail Record"
date: 2025-01-01
abbr: "IPDR"
fullName: "Internet Protocol Detail Record"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ipdr/"
summary: "Standardizovaný formát datového záznamu používaný pro fakturaci, účetnictví a analýzu síťového provozu v IP telekomunikačních sítích. IPDR zachycuje podrobné informace o využití síťové servisní relace"
---

IPDR je standardizovaný formát datového záznamu používaný v IP telekomunikačních sítích pro zachycení podrobných informací o servisní relaci pro účely fakturace, účetnictví a analýzy provozu.

## Popis

Internet Protocol Detail Record (IPDR) je komplexní rámec a datový formát definovaný 3GPP pro zaznamenávání informací o využití služeb v IP sítích. Je základním kamenem architektury účtování 3GPP, konkrétně v rámci Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)). IPDR je generován síťovými funkcemi, které poskytují nebo umožňují službu, jako je Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN), Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) nebo Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)). Každý záznam dokumentuje samostatnou událost nebo relaci využití služby a poskytuje podrobný, strojově čitelný přehled o tom, co bylo spotřebováno, kým, kdy a za jakých podmínek.

Architektura generování a přenosu IPDR zahrnuje několik klíčových komponent. Charging Trigger Function ([CTF](/mobilnisite/slovnik/ctf/)), vestavěná v síťovém prvku (např. v PGW), detekuje zpoplatnitelné události na základě předdefinovaných pravidel. Když k takové události dojde (např. zřízení [IP-CAN](/mobilnisite/slovnik/ip-can/) relace, dosažení objemového prahu, detekce toku služebních dat), CTF shromáždí příslušné účtovací informace a naformátuje je do IPDR. Tento IPDR je poté streamován téměř v reálném čase přes referenční bod Rf (pro offline účtování) do Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)). CDF záznamy ověří, konsoliduje a případně koreluje více IPDR, než je jako Charging Data Records ([CDR](/mobilnisite/slovnik/cdr/)) předá do Charging Gateway Function (CGF) a nakonec do fakturační domény operátora.

IPDR se skládá ze strukturované sady polí definovaných v 3GPP TS 32.297. Jeho schéma je rozšiřitelné, aby pokrylo různé služby (např. IMS, MMS, datovou konektivitu). Mezi běžná pole patří jedinečný identifikátor záznamu, identita účastníka (např. IMSI, MSISDN), adresa obsluhujícího síťového prvku, časy začátku a ukončení relace, objemy odeslaných a přijatých dat, aplikované parametry QoS, identifikátory ratingových skupin a služebně specifické informace. Formát je navržen tak, aby byl jednoznačný a úplný, a zajistil tak fakturačnímu systému veškeré potřebné informace pro aplikaci správného tarifu.

Fungování IPDR je nedílnou součástí moderního využitím řízeného účtování. Například během mobilní datové relace uživatele může PGW vygenerovat IPDR při zahájení relace, průběžné IPDR v určitých objemových intervalech (např. každých 10 MB) a konečný IPDR při ukončení relace. Tento proud záznamů poskytuje detailní stopu využití. Protokol pro přenos těchto záznamů (IPDR Streaming Protocol) zajišťuje spolehlivé a uspořádané doručení z CTF do CDF. Úlohou IPDR je tedy poskytovat nezpracovaná, faktická data o spotřebě síťových zdrojů, která jsou zásadním vstupem pro všechny následné procesy účtování, fakturace, analýz a správy podvodů v obchodním ekosystému telekomunikačního operátora.

## K čemu slouží

IPDR byl vytvořen, aby řešil kritickou potřebu standardizovaného, flexibilního a spolehlivého mechanismu pro zachycení dat o využití v stále složitějších IP telekomunikačních službách. Před jeho standardizací používali dodavatelé a operátoři často proprietární formáty pro záznamy o využití, což vedlo k problémům s interoperabilitou, vysokým nákladům na integraci a omezené flexibilitě při zavádění nových služeb. Jak se sítě 3GPP vyvíjely od jednoduchých hlasových hovorů k nabízení paketových dat, multimediálních služeb IMS a diferencované QoS, požadovaná účtovací data se stala mnohem složitějšími než tradiční call detail records (CDR) pro přepojování okruhů.

Motivace pro IPDR vycházela z komerční nutnosti přesně a efektivně zpoplatňovat tyto nové IP služby. Operátoři potřebovali podporovat různé fakturační modely: objemové, časové, událostní a specifické pro služby. Standardizovaný formát podrobného záznamu byl nezbytný pro umožnění více-dodavatelských sítí, kde GGSN od jednoho dodavatele musí odesílat data o využití do účtovacího systému od jiného dodavatele. IPDR poskytl tento společný jazyk. Vyřešil problém, jak reprezentovat heterogenní využití služeb (prohlížení webu, streamování videa, IMS hovor) v homogenním, strukturovaném záznamu, který mohou následné fakturační a analytické systémy automaticky zpracovávat.

Zavedený ve Release 8 byl IPDR součástí širší přestavby architektury účtování 3GPP pro podporu vize All-IP sítě v rámci EPS (Evolved Packet System). Nahradil a zobecnil dřívější, méně flexibilní formáty záznamů. Poskytnutím streamovacího rozhraní (Rf) a dobře definovaného schématu umožnil sběr dat téměř v reálném čase, což bylo klíčové pro včasné účtování, kontrolu výdajových limitů a analýzy v reálném čase. Jeho vytvoření bylo hnací silou požadavku oddělit vývoj sítě od vývoje fakturačního systému, což umožnilo nasazovat nové služby bez nutnosti úprav jádra fakturační infrastruktury, pokud byly schopny generovat kompatibilní IPDR.

## Klíčové vlastnosti

- Standardizované, rozšiřitelné schéma založené na XML pro reprezentaci různorodých dat o využití služeb
- Podporuje streamovací přenosový protokol (přes Diameter Rf) pro doručování záznamů téměř v reálném čase
- Zachycuje detailní informace: objemy dat, časová razítka relace, identifikátory účastníka, parametry QoS, identifikátory služeb
- Umožňuje flexibilní účtovací modely (objemové, časové, událostní, kombinované)
- Základní komponenta 3GPP Offline Charging System (OFCS)
- Poskytuje dodavatelům nezávislé rozhraní mezi síťovými prvky a účtovacími systémy

## Definující specifikace

- **TS 32.297** (Rel-19) — Charging Data Record File Transfer

---

📖 **Anglický originál a plná specifikace:** [IPDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipdr/)
