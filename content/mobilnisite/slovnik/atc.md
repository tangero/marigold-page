---
slug: "atc"
url: "/mobilnisite/slovnik/atc/"
type: "slovnik"
title: "ATC – Ancillary Terrestrial Component"
date: 2022-01-01
abbr: "ATC"
fullName: "Ancillary Terrestrial Component"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/atc/"
summary: "ATC je pozemní síťová komponenta, která doplňuje satelitní sítě tím, že poskytuje pokrytí v oblastech, kde je satelitní signál blokován, například v městských kaňonech nebo vnitřních prostorech. Umožň"
---

ATC je pozemní síťová komponenta, která doplňuje satelitní sítě tím, že poskytuje pokrytí v oblastech, kde je satelitní signál blokován, a zajišťuje tak plynulou kontinuitu služeb.

## Popis

Ancillary Terrestrial Component (ATC) je klíčový architektonický prvek v rámci Neterestriálních sítí ([NTN](/mobilnisite/slovnik/ntn/)) podle 3GPP, který je speciálně navržen pro integraci pozemní buněčné infrastruktury se satelitními sítěmi. Funguje jako pozemní uzel rádiového přístupu, který slouží jako rozšíření satelitní sítě, využívá licencované spektrum přidělené pro satelitní služby, ale používá pozemní přenosové techniky. ATC se připojuje k jádru sítě prostřednictvím standardních pozemních rozhraní (jako [N2](/mobilnisite/slovnik/n2/)/N3 pro 5G), ale jeho rádiové rozhraní je sladěno se satelitní komponentou, aby poskytlo jednotný uživatelský zážitek. Tento dvou režimový provoz vyžaduje sofistikované mechanismy synchronizace a předávání spojení mezi satelitními a pozemními paprsky.

Z architektonického hlediska může být ATC implementován jako vyhrazená základnová stanice (gNB v 5G) nebo jako specializovaná funkce v rámci existujícího uzlu pozemní sítě. Zahrnuje modifikované algoritmy správy rádiových zdrojů pro zvládnutí jedinečných charakteristik integrace satelit-pozemní síť, jako jsou delší zpoždění šíření a různé Dopplerovy efekty ve srovnání s čistě pozemními systémy. Rádiový přenos ATC je pečlivě řízen, aby se předešlo interferencím se satelitní komponentou, často za použití komplementárních charakteristik paprsků nebo koordinace frekvence/výkonu. Mezi klíčové komponenty patří rádiová jednotka ATC (s vlnovými formami kompatibilními se satelitem), jednotka základního pásma ATC a funkce pro vzájemné propojení, která spravuje rozhraní mezi řídicími rovinami pozemní a satelitní sítě.

Při provozu ATC poskytuje pokrytí v konkrétních geografických oblastech, kde jsou satelitní signály nespolehlivé – typicky v hustě zastavěných městských prostředích s vysokými budovami, v podzemních prostorách nebo vnitřních prostorech se špatnou viditelností satelitu. Když uživatelské zařízení (UE) detekuje nízkou kvalitu satelitního signálu, síť může iniciovat předání spojení na ATC pomocí standardních 3GPP procedur mobility, ačkoli s vylepšenými algoritmy, které zohledňují rozdílné topologie sítí. ATC se pro UE jeví jako součást stejné logické sítě jako satelit, čímž zachovává kontinuitu relace a kvalitu služeb. Pro vysílání ve směru k síti (uplink) ATC agreguje uživatelská data a přeposílá je přes pozemní páteřní síť do jádra sítě, zatímco pro příjem ze sítě (downlink) přijímá data z jádra sítě a vysílá je lokálně k UE ve své oblasti pokrytí.

ATC hraje zásadní roli při zpřístupňování služeb založených na satelitech pro masové aplikace tím, že řeší základní omezení satelitních signálů blokovaných fyzickými překážkami. Umožňuje poskytovatelům služeb nabízet garantované pokrytí i v náročných prostředích, aniž by uživatelé potřebovali dvou režimová zařízení se samostatnými satelitními a pozemními rádiovými moduly. Integrace je řízena na úrovni sítě, přičemž ATC a satelitní komponenty jsou koordinovány prostřednictvím řídicí roviny sítě za účelem optimalizace využití zdrojů a zachování konzistentního uplatňování politik napříč oběma typy přístupu.

## K čemu slouží

ATC bylo vytvořeno za účelem řešení základních omezení pokrytí komunikačních systémů založených na satelitech, zejména pro mobilní služby cílené na spotřebitele a zařízení IoT. Tradiční satelitní sítě mají potíže s poskytováním spolehlivé služby v městských kaňonech, vnitřních prostorech a dalších prostředích, kde je přímá viditelnost satelitů blokována. Před zavedením ATC řešení spočívala buď v akceptaci mezer v pokrytí (nepřijatelné pro služby kritické z hlediska bezpečnosti), nebo v nasazení zcela oddělených pozemních sítí (nákladné a neefektivní). ATC poskytuje integrovaný přístup, který zachovává výhody satelitů v podobě rozsáhlého pokrytí a zároveň vyplňuje kritické mezery cíleným pozemním nasazením.

Motivace pro vývoj ATC v 3GPP Release 15 vycházela z rostoucího zájmu o služby globální konektivity, zejména pro aplikace IoT, námořní a letecké služby a širokopásmové připojení ve venkovských oblastech. Satelitní operátoři potřebovali způsob, jak rozšířit své služby do prostředí, kde bylo čistě satelitní pokrytí nepraktické, zatímco pozemní operátoři usilovali o využití satelitního spektra pro doplňkové pokrytí. Předchozí přístupy, jako hybridní satelitně-pozemní sítě, často fungovaly jako oddělené systémy s různým přidělením spektra, což vyžadovalo složitá dvou režimová zařízení a manuální výběr sítě. ATC standardizuje integraci na úrovni síťové architektury a umožňuje plynulou kontinuitu služeb bez nutnosti speciálního uživatelského zařízení.

ATC řeší několik konkrétních omezení: Za prvé řeší problém pokrytí ve městech, kde útlum prostupem budovami činí satelitní signály nepoužitelnými uvnitř budov. Za druhé umožňuje spolehlivé nouzové komunikace v katastrofických scénářích, kdy satelit může být jedinou přežívající infrastrukturou, ale stále potřebuje lokální distribuci. Za třetí umožňuje efektivnější využití vzácného satelitního spektra přesměrováním provozu na pozemní komponenty v hustě obydlených oblastech. Technologie byla zvláště motivována regulačním vývojem umožňujícím satelitním operátorům nasazovat doplňkové pozemní komponenty ve svém licencovaném spektru, což vytváří nové obchodní modely pro integrované poskytovatele satelitně-pozemních služeb.

## Klíčové vlastnosti

- Plynulé předávání spojení mezi satelitní a pozemní komponentou
- Využití spektra přiděleného pro satelity pro pozemní přenos
- Integrovaná řídicí rovina se satelitní sítí
- Rozšířený management mobility pro hybridní síťové topologie
- Koordinace rušení mezi satelitními a pozemními paprsky
- Podpora pro standardní 3GPP UE bez úprav specifických pro satelit

## Definující specifikace

- **TS 22.825** (Rel-16) — UAS Remote Identification and Tracking over 3GPP
- **TR 22.829** (Rel-17) — Enhancement for UAVs; Stage 1
- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 23.754** (Rel-17) — Study on UAS Connectivity, ID & Tracking
- **TS 23.790** (Rel-15) — FRMCS Gap Analysis and Architecture Enhancements
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US

---

📖 **Anglický originál a plná specifikace:** [ATC na 3GPP Explorer](https://3gpp-explorer.com/glossary/atc/)
