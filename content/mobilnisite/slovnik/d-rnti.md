---
slug: "d-rnti"
url: "/mobilnisite/slovnik/d-rnti/"
type: "slovnik"
title: "D-RNTI – Drift Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "D-RNTI"
fullName: "Drift Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/d-rnti/"
summary: "Dočasný identifikátor přidělený driftovým řadičem rádiové sítě (Drift RNC) uživatelskému zařízení (UE) během mezilehlého přechodu mezi RNC typu soft handover v síti UTRAN. Jednoznačně identifikuje spo"
---

D-RNTI je dočasný identifikátor přidělený driftovým RNC (Drift RNC) uživatelskému zařízení (UE) během mezilehlého přechodu mezi RNC typu soft handover, který jednoznačně identifikuje spojení na rozhraní Iur.

## Popis

Drift Radio Network Temporary Identifier (D-RNTI) je základní identifikátor specifický pro uživatelské zařízení (UE) používaný v architektuře Universal Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), který je konkrétně definován pro provoz na rozhraní Iur. Toto rozhraní spojuje dva řadiče rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)): obsluhující RNC ([SRNC](/mobilnisite/slovnik/srnc/)), které drží hlavní řídicí spojení ([RRC](/mobilnisite/slovnik/rrc/) spojení) k UE, a driftové RNC ([DRNC](/mobilnisite/slovnik/drnc/)), které řídí jeden nebo více Node B (základnových stanic), k nimž je UE během soft handoveru dodatečně připojeno. D-RNTI je přiděleno DRNC v okamžiku, kdy UE naváže rádiový spoj přes buňku pod kontrolou tohoto DRNC, zatímco SRNC zůstává hlavní řídicí entitou. Toto přidělení je sděleno z DRNC do SRNC prostřednictvím signalizačních zpráv na rozhraní Iur, například těch používaných pro nastavení nebo přidání rádiového spoje.

Z provozního hlediska slouží D-RNTI jako lokální identifikátor v kontextu konkrétního DRNC a instance rozhraní Iur. Používá se k jednoznačné adresaci UE ve všech následných signalizačních přenosech a přenosech uživatelských dat, které procházejí rozhraním Iur a týkají se spojení daného UE. Například když je třeba přeposlat rámce uživatelské roviny (Frame Protocol data frames) ze SRNC do DRNC pro vysílání k UE přes přidaný rádiový spoj, je D-RNTI zahrnuto do hlaviček rámců, aby DRNC mohlo data správně směrovat do příslušného kontextu UE a na odpovídající rádiový spoj. Podobně jsou měřicí reporty nebo jiné řídicí informace z DRNC směrem k SRNC týkající se této konkrétní UE označeny D-RNTI.

Rozsah platnosti tohoto identifikátoru je striktně omezen na spojení na rozhraní Iur mezi konkrétní dvojicí SRNC a DRNC pro dané UE. Samotné UE tento identifikátor nezná, jde čistě o interní síťový identifikátor pro správu rozhraní Iur. Použití dočasného identifikátoru přiděleného DRNC, jako je D-RNTI, je klíčové pro oddělení primárního identifikátoru UE na straně SRNC ([S-RNTI](/mobilnisite/slovnik/s-rnti/)) od interní správy zdrojů v DRNC. Umožňuje DRNC spravovat své rádiové spoje pro UE pomocí vlastního adresovacího schématu bez nutnosti globální koordinace hodnot [RNTI](/mobilnisite/slovnik/rnti/) v celé síti, což zjednodušuje správu zdrojů a škálovatelnost v prostředí s více RNC.

## K čemu slouží

D-RNTI bylo vytvořeno pro řešení specifických požadavků na signalizaci a směrování dat, které přinesly soft handover a makrodiverzita v sítích UMTS [UTRAN](/mobilnisite/slovnik/utran/), zejména když je UE v komunikaci s buňkami řízenými různými RNC. Před UMTS byly přechody v GSM typicky hard handovery s jednoduššími postupy typu 'přeruš a pak naváž' (break-before-make), které nevyžadovaly složité současné přeposílání dat mezi více řadiči. Rozhraní UMTS WCDMA umožnilo soft handover, kdy může být UE současně připojena k více buňkám za účelem zlepšení spolehlivosti a kvality. Tato schopnost zavedla architektonický koncept SRNC a DRNC, když tyto buňky patří pod různá RNC, což si vyžádalo standardizované mezilehlé rozhraní (Iur) pro koordinaci.

Základní problém, který D-RNTI řeší, je potřeba efektivní a jednoznačné identifikace kontextu konkrétního UE na rozhraní Iur. Bez vyhrazeného identifikátoru, jako je D-RNTI, by musely DRNC a SRNC spoléhat na jiné, méně efektivní mechanismy pro korelaci zpráv a datových rámců pro UE, například používání dlouhých, globálně unikátních identit UE (jako IMSI) v každém přenosu, což by významně zvýšilo signalizační režii. D-RNTI poskytuje kompaktní, dočasnou 'rukojeť', kterou může DRNC přidělit lokálně. Umožňuje DRNC udržovat lokální kontext UE (spojený s rádiovými zdroji) a umožňuje SRNC přesně adresovat tento kontext za účelem přeposílání dat ve směru downlink nebo přijímání dat a měření ve směru uplink. Tento mechanismus je nezbytný pro udržení plynulého toku uživatelských dat a řídicí signalizace během mezilehlého soft handoveru mezi RNC, což je klíčová vlastnost pro udržení kvality hovoru a spolehlivosti sítě v UMTS.

## Klíčové vlastnosti

- Jednoznačně identifikuje kontext spojení UE na rozhraní Iur mezi SRNC a DRNC.
- Přiděluje jej driftové RNC (DRNC) během procedur nastavení nebo přidání mezilehlého rádiového spoje mezi RNC.
- Používá se pro adresování jak v signalizaci řídicí roviny, tak při směrování datových rámců uživatelské roviny přes rozhraní Iur.
- Jeho platnost je lokální pro konkrétní instanci rozhraní Iur a DRNC, které jej přidělilo.
- Umožňuje efektivní kombinování makrodiverzity a přeposílání dat během mezilehlého soft handoveru mezi RNC v síti UTRAN.
- Jde o dočasný identifikátor, který je uvolněn při odstranění přidružených rádiových spojů k DRNC.

## Související pojmy

- [S-RNTI – Serving Radio Network Temporary Identifier](/mobilnisite/slovnik/s-rnti/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols

---

📖 **Anglický originál a plná specifikace:** [D-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/d-rnti/)
