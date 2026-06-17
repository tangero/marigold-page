---
slug: "iv"
url: "/mobilnisite/slovnik/iv/"
type: "slovnik"
title: "IV – Interference Variable"
date: 2025-01-01
abbr: "IV"
fullName: "Interference Variable"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iv/"
summary: "Vypočítaná proměnná (Nu) používaná ve specifikacích 3GPP, zejména pro UMTS, k hodnocení a řízení rušení v uplinku. Je odvozena z frekvence uplinku (FUL) a je klíčovým parametrem při plánování rádiové"
---

IV je vypočítaná proměnná používaná ve specifikacích 3GPP pro UMTS k hodnocení a řízení rušení v uplinku, která ovlivňuje regulaci výkonu a překládání buňky při plánování sítě.

## Popis

Proměnná rušení (Interference Variable – IV), často označovaná jako Nu, je základní parametr definovaný v Technických specifikacích 3GPP pro sítě UMTS (Universal Mobile Telecommunications System). Nejde o fyzické měření, ale o vypočítanou hodnotu používanou jako vstup pro různé algoritmy řízení rádiových zdrojů (RRM). Primární definice je dána vzorcem Nu = 5 * (FUL – 1480,1 MHz), kde FUL je nosná frekvence uplinku v MHz. Tento vzorec stanovuje lineární vztah mezi provozní frekvencí a standardizovanou proměnnou rušení.

Z architektonického hlediska se výpočet IV provádí v nástrojích pro plánování rádiové sítě a potenciálně v softwaru RNC (Radio Network Controller) či Node B (základnové stanice). Slouží jako normalizovaná metrika, která zohledňuje skutečnost, že charakteristiky šíření rádiového signálu a náchylnost k rušení se s frekvencí mění. Vyšší FUL vede k vyšší hodnotě Nu, která kvantitativně reprezentuje zvýšený útlum na dráze a odlišný profil rušení očekávaný v daném frekvenčním pásmu. To umožňuje navrhovat RRM algoritmy obecně, přičemž Nu slouží jako zástupný ukazatel pro frekvenčně závislé efekty namísto pevného zakódování chování pro konkrétní pásma.

V praxi se IV (Nu) používá ve specifikacích upravujících oblasti, jako je koordinace rušení v uplinku, řízení přístupu a řízení zatížení. Například může být součástí výpočtů určujících práh rušení v uplinku (RoT – Rise over Thermal), který buňka snese, nebo v algoritmech pro mezifrekvenční předávání hovoru. Zahrnutím Nu se tyto algoritmy automaticky přizpůsobí, ať je síť nasazena v pásmu 900 MHz, 2100 MHz či jiných UMTS pásmech, čímž je zajištěn konzistentní výkon a stabilita. Jeho výskyt v mnoha specifikacích (např. 25.141 pro shodu základnových stanic, 33.204 pro zabezpečení, 35.909 pro koexistenci LTE a UMTS) podtrhuje jeho roli jakožto průřezového parametru pro modelování výkonu a zabezpečení sítě.

## K čemu slouží

Proměnná rušení byla vytvořena, aby poskytla standardizovaný, na frekvenci citlivý parametr pro řízení rádiových zdrojů v UMTS. Rané buněčné systémy často používaly algoritmy naladěné na konkrétní frekvenční pásma, což se stalo nepraktickým, když operátoři získávali spektrum v různorodých pásmech (např. 850, 900, 1900, 2100 MHz). Útlum rádiového signálu s rostoucí frekvencí roste, což znamená, že signál na 2100 MHz slábne rychleji než signál na 900 MHz. To přímo ovlivňuje úroveň rušení, dosah buňky a regulaci výkonu.

Před zavedením takové standardizované proměnné mohli dodavatelé síťového zařízení používat konstanty specifické pro pásma nebo složité proprietární vzorce, což komplikovalo testování interoperability a předpovědi konzistentního výkonu sítě. Vzorec pro IV poskytuje jednoduchý a deterministický způsob škálování chování RRM na základě základní fyzikální vlastnosti nosné frekvence. Abstrahuje frekvenční závislost do jedné proměnné (Nu), což umožňuje specifikacím definovat univerzální algoritmy, které správně fungují napříč celosvětovou mozaikou UMTS frekvenčních alokací.

Její účel sahá i do oblasti zabezpečení sítě a koexistence. Ve specifikacích jako 33.204 a 33.210 se parametry související s IV používají při odvozování kryptografických klíčů pro ochranu integrity, čímž se propojuje zabezpečení s fyzickým rádiovým prostředím. Ve specifikaci 35.909 napomáhá při modelování rušení mezi systémy LTE a UMTS pracujícími na sousedních kanálech či pásmech a zajišťuje tak jejich pokojnou koexistenci. IV tedy řeší problém návrhu RRM nezávislého na frekvenci a umožňuje robustní, škálovatelný a standardizovaný provoz sítě.

## Klíčové vlastnosti

- Frekvenčně závislý výpočet: Přímo odvozeno z nosné frekvence uplinku (FUL) pomocí vzorce Nu = 5 * (FUL – 1480,1 MHz).
- Normalizační faktor: Slouží jako škálovací faktor pro normalizaci efektů rušení a šíření napříč různými frekvenčními pásmy.
- Vstup pro RRM algoritmy: Klíčový parametr pro koordinaci rušení v uplinku, řízení přístupu a procedury řízení zatížení v RNC a Node B.
- Relevance napříč specifikacemi: Odkazováno ve specifikacích pokrývajících testování shody, zabezpečení a rádiovou koexistenci.
- Deterministické a jednoduché: Poskytuje jasnou a jednoznačnou hodnotu pro jakékoli dané FUL, čímž zajišťuje konzistentní implementaci.
- Umožňuje obecný návrh: Umožňuje návrh algoritmů řízení rádiových zdrojů obecně, nezávisle na konkrétních provozních pásmech.

## Definující specifikace

- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 29.204** (Rel-19) — SS7 Security Gateway Functional Description
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report

---

📖 **Anglický originál a plná specifikace:** [IV na 3GPP Explorer](https://3gpp-explorer.com/glossary/iv/)
