---
slug: "ppd"
url: "/mobilnisite/slovnik/ppd/"
type: "slovnik"
title: "PPD – Paging Policy Differentiation"
date: 2026-01-01
abbr: "PPD"
fullName: "Paging Policy Differentiation"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ppd/"
summary: "PPD (Paging Policy Differentiation) je funkce 5G, která umožňuje síti aplikovat různé strategie pagingu na základě typu služby, stavu UE nebo síťových podmínek. Optimalizuje signalizační zátěž pagingu"
---

PPD je funkce 5G, která umožňuje síti aplikovat různé strategie pagingu na základě typu služby, stavu UE nebo síťových podmínek za účelem optimalizace signalizační zátěže a zvýšení pravděpodobnosti úspěšného pagingu.

## Popis

Paging Policy Differentiation (PPD) je mechanismus zavedený v systému 5G (5GS), který umožňuje diferencované zpracování procedur pagingu na základě různých politik. Funguje uvnitř funkce pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5G core síti, která je zodpovědná za zahájení pagingu při příchodu downlink dat nebo signalizace pro UE v idle nebo inactive módu. PPD umožňuje AMF vybrat z více pagingových strategií, z nichž každá je definována sadou konfigurovatelných parametrů, aby se optimalizoval výkon pro konkrétní scénáře.

Jak to funguje: AMF obdrží oznámení o downlink datech od User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) nebo žádost o signalizaci od jiné síťové funkce. AMF vyhodnotí atributy, jako je Data Network Name ([DNN](/mobilnisite/slovnik/dnn/)), Single-Network Slice Selection Assistance Information ([S-NSSAI](/mobilnisite/slovnik/s-nssai/)), charakteristiky QoS Flow nebo data o předplatném UE, aby určila vhodnou pagingovou politiku. Politiky mohou určovat varianty v rozsahu pagingové oblasti (např. buňka, seznam sledovacích oblastí nebo celá registrační oblast), počtu pokusů o paging, časového intervalu mezi opakováními a použití indikátorů priority. Například politika pro ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) může spustit paging v menší oblasti s rychlejšími opakováními, zatímco politika pro massive IoT může využívat širší oblasti s menším počtem pokusů k úspoře signalizace.

Klíčové komponenty zahrnují Paging Policy Indicator ([PPI](/mobilnisite/slovnik/ppi/)), který může být signalizován mezi síťovými funkcemi k předání zvolené politiky, a procedury rozhraní N1/[N2](/mobilnisite/slovnik/n2/), které přenášejí pagingové zprávy k Next-Generation Node B (gNB). Architektura se integruje s Network Slicing, protože různé slice mohou mít odlišné pagingové politiky odpovídající jejich smlouvám o úrovni služeb. AMF využívá lokální konfiguraci nebo pokyny od funkce pro řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) k mapování požadavků služby na pagingové parametry. Dále může PPD interagovat s optimalizací pagingu v RAN pro inactive mód, kde RAN může uchovávat kontext UE a pomáhat s pagingem zohledňujícím polohu.

Jeho role spočívá v tom, aby byl paging v 5G inteligentnější a efektivnější ve srovnání s jednotným přístupem předchozích generací. Diferencováním politik může síť vyvážit protichůdné cíle: minimalizovat signalizační zátěž pagingu ke snížení přetížení, maximalizovat pravděpodobnost úspěchu pagingu pro splnění cílů latence a šetřit výdrž baterie UE. To je obzvláště kritické v různorodých scénářích nasazení 5G, které sahají od enhanced mobile broadband s vysokou koncentrací uživatelů po průmyslové IoT s masivním počtem zařízení. PPD tak přispívá k celkové škálovatelnosti a služebně orientovanému provozu 5G core sítě.

## K čemu slouží

PPD bylo vytvořeno k řešení omezení jednotných pagingových mechanismů v LTE, které nemohly efektivně pojmout širokou škálu služeb a požadavků plánovaných pro 5G. V 4G byly pagingové parametry z velké části statické nebo založené na jednoduchých kategoriích UE, což vedlo k neoptimálnímu výkonu pro extrémní případy užití, jako jsou massive machine-type communications nebo služby s kritickými požadavky. Jednotný přístup vedl buď k nadměrné signalizační režii, nebo k nedostatečné spolehlivosti pro určité aplikace.

Řeší problém neefektivního využití zdrojů během správy mobility pro heterogenní služby. Například paging zařízení massive IoT se stejnou naléhavostí jako hovor plýtvá síťovými zdroji, zatímco paging autonomního vozidla se stejnou volností jako u senzoru může způsobit nebezpečná zpoždění. PPD zavádí detailní kontrolu, která umožňuje síti přizpůsobit chování pagingu specifickým potřebám každého typu služby, slice nebo QoS flow. Tato optimalizace snižuje signalizační zátěž v core a RAN, což je zásadní pro podporu předpokládaného rozsahu 5G připojení.

Motivace vychází z klíčových principů návrhu 5G: služebně orientované architektury a network slicing. Protože má 5G sloužit vertikálním odvětvím s přísnými a různorodými požadavky, musí core síť zacházet s různými třídami provozu odlišně. PPD poskytuje nástroje k implementaci této diferenciace v doméně pagingu, což je základní procedura mobility. Historický kontext zahrnuje vývoj od základního pagingu v 2G/3G k mírně vylepšenému pagingu v LTE s funkcemi jako je priorizace pagingu, ale PPD v 5G představuje systematický, politikami řízený rámec. Umožňuje operátorům nasadit přizpůsobené pagingové strategie, které jsou v souladu s obchodními politikami, regulatorními požadavky a technickými omezeními, čímž zvyšuje celkovou efektivitu sítě a uživatelský zážitek.

## Klíčové vlastnosti

- Umožňuje služebně orientované pagingové strategie založené na DNN, S-NSSAI nebo QoS flows
- Konfigurovatelné parametry zahrnují rozsah pagingové oblasti, počet opakování a intervaly mezi opakováními
- Podporuje Paging Policy Indicator (PPI) pro komunikaci politiky mezi funkcemi
- Integruje se s 5G Network Slicing pro pagingové chování specifické pro slice
- Snižuje signalizační přetížení optimalizací počtu pagingových pokusů podle typu služby
- Zvyšuje pravděpodobnost úspěchu pagingu pro aplikace citlivé na latenci

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [S-NSSAI – Single Network Slice Selection Assistance Information](/mobilnisite/slovnik/s-nssai/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2

---

📖 **Anglický originál a plná specifikace:** [PPD na 3GPP Explorer](https://3gpp-explorer.com/glossary/ppd/)
