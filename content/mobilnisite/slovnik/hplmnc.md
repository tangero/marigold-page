---
slug: "hplmnc"
url: "/mobilnisite/slovnik/hplmnc/"
type: "slovnik"
title: "HPLMNC – Home Public Land Mobile Network of the C subscriber"
date: 2025-01-01
abbr: "HPLMNC"
fullName: "Home Public Land Mobile Network of the C subscriber"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hplmnc/"
summary: "HPLMN třetí strany (účastníka C) zapojené do komunikační služby, například ve scénáři přesměrování hovoru nebo konference. Identifikuje domovskou síť strany odlišné od primárního volajícího (A) nebo v"
---

HPLMNC je domácí veřejná pozemní mobilní síť (Home Public Land Mobile Network) třetí strany (účastníka C) zapojené do komunikační služby; používá se k identifikaci domovské sítě této strany pro specializované směrování a řízení služeb.

## Popis

Domácí veřejná pozemní mobilní síť účastníka C (HPLMNC) je specializovaný identifikátor používaný v telekomunikačních scénářích zahrnujících tři a více stran. 'Účastník C' typicky označuje třetí stranu zavedenou do komunikační relace, nejčastěji při přesměrování hovoru, přepojení hovoru nebo konferenčním hovoru s více účastníky. Například, pokud účastník A volá účastníkovi B a B má aktivní bezpodmínečné přesměrování hovoru na účastníka C, pak C je účastník C. HPLMNC je domovská síť tohoto účastníka, na kterého je hovor přesměrován nebo přepojen. Jeho identifikace je nezbytná, aby síť mohla hovor správně směrovat k C, autentizovat a autorizovat účast C a aplikovat správnou servisní logiku a účtování pro tuto třetí větev hovoru.

Z architektonického hlediska potřeba HPLMNC vzniká v rámci síťových uzlů, které zpracovávají složité modely stavu hovoru, jako jsou Service Switching Functions ([SSF](/mobilnisite/slovnik/ssf/)) v tradičních okruzích, [MSC](/mobilnisite/slovnik/msc/) servery, nebo Media Resource Function Controller ([MRFC](/mobilnisite/slovnik/mrfc/)) a Application Servers ([AS](/mobilnisite/slovnik/as/)) v IMS. Když má být hovor přesměrován nebo je iniciována konference, řídicí síťový prvek musí provést analýzu směrování pro nový cíl (účastníka C). To zahrnuje extrakci nebo určení HPLMNC z [MSISDN](/mobilnisite/slovnik/msisdn/) nebo [IMSI](/mobilnisite/slovnik/imsi/) účastníka C. Uzel pak může potřebovat dotazovat [HLR](/mobilnisite/slovnik/hlr/) nebo [HSS](/mobilnisite/slovnik/hss/) v HPLMNC, aby získal roamingové číslo (MSRN) nebo zkontroloval autorizaci služby, podobně jako u účastníka B, ale nyní v sekundární, odvozené větvi hovoru.

Operační role HPLMNC je úzce spojena s doplňkovými službami a funkcemi inteligentní sítě. V prostředí řízeném CAMEL může detekční bod pro přesměrování hovoru spustit dialog s SCP. HPLMNC je v tomto dialogu cennou informací, protože logika SCP může záviset na vztahu mezi sítěmi (např. zda je přesměrování na číslo v rámci vlastní sítě nebo mimo ni, což ovlivňuje náklady). V IMS musí MRFC a AS při řízení relace a potenciálně při aplikaci politik specifických pro účastníka zohlednit HPLMNC každého účastníka (mimo první dva). Zpracování HPLMNC zajišťuje, že síť může rozšířit servisní logiku za rámec jednoduchých bod-bod hovorů a podporovat bohatou sadu doplňkových služeb, které definují moderní telekomunikace.

## K čemu slouží

Účelem definice HPLMNC je rozšířit princip identifikace a řízení domovské sítě na všechny strany zapojené do složité komunikační služby, nejen na primární dvě. Rané přesměrování hovoru bylo jednoduchým přepojením na úrovni přepínače. Avšak se zavedením služeb řízených účastníkem, předplaceného účtování a zúčtování mezi operátory se stalo klíčové identifikovat a zacházet s každou větví komunikace nezávisle. Účastník C není pouze koncovým bodem směrování, ale plnohodnotným účastníkem s vlastní HPLMN, servisním profilem a fakturačním vztahem.

Toto řeší specifické technické a komerční výzvy. Technicky umožňuje vyvolat správnou servisní logiku pro účastníka C. Například, pokud má C ve své HPLMN aktivní službu 'nerušit', síť potřebuje identifikovat HPLMNC, aby tuto blokaci aplikovala. Komerčně umožňuje přesné účtování. Náklady na hovor přesměrovaný na mezinárodní číslo (účastník C) se velmi liší od hovoru přesměrovaného lokálně. Identifikací HPLMNC může síť určit vhodné mezisíťové poplatky pro větev k C. Koncept formalizuje zacházení s terciárními stranami v rámci signalizačních standardů a zajišťuje interoperabilitu mezi operátory, když složité scénáře hovorů překračují více sítí.

## Klíčové vlastnosti

- Identifikuje domovskou síť třetí strany (účastníka C) ve službách komunikace s více větvemi
- Používá se při přesměrování hovoru (CFU, CFB, CFNRy), explicitním přepojení hovoru a zakládání konferenčních hovorů
- Umožňuje směrovací dotazy na HLR/HSS účastníka C za účelem získání adresy aktuálně obsluhujícího uzlu
- Poskytuje kontext pro servisní logiku inteligentní sítě (CAMEL) ovlivňující větev strany C
- Podporuje přesné účtování a zúčtování mezi operátory za další větev hovoru k účastníkovi C
- Zajišťuje, že vlastní předplacené služby a politiky účastníka C mohou být aplikovány, když je tento účastník zaveden do relace

## Související pojmy

- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [HPLMNB – Home Public Land Mobile Network of the B subscriber](/mobilnisite/slovnik/hplmnb/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [HPLMNC na 3GPP Explorer](https://3gpp-explorer.com/glossary/hplmnc/)
