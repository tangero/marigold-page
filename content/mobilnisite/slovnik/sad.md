---
slug: "sad"
url: "/mobilnisite/slovnik/sad/"
type: "slovnik"
title: "SAD – Security Association Database"
date: 2025-01-01
abbr: "SAD"
fullName: "Security Association Database"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sad/"
summary: "Databáze udržovaná síťovým uzlem (např. bránou, firewallem), která ukládá parametry aktivních bezpečnostních asociací (SA). Obsahuje kryptografické klíče, algoritmy, životnosti a další kontext potřebn"
---

SAD je databáze, která ukládá parametry aktivních bezpečnostních asociací (Security Associations), včetně kryptografických klíčů, algoritmů a životností, pro zabezpečení komunikací pomocí IPsec nebo jiných bezpečnostních protokolů.

## Popis

Databáze bezpečnostních asociací (Security Association Database – SAD), někdy označovaná jako SADB, je klíčovou součástí implementace bezpečnostních protokolů, jako je [IPsec](/mobilnisite/slovnik/ipsec/) (Internet Protocol Security). V architekturách 3GPP ji udržují síťové entity, jako je Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)), Trusted [WLAN](/mobilnisite/slovnik/wlan/) Access Gateway ([TWAG](/mobilnisite/slovnik/twag/)) nebo bezpečnostní brány, které používají IPsec k ochraně uživatelských dat nebo provozu řídicí roviny. Bezpečnostní asociace ([SA](/mobilnisite/slovnik/sa/)) je soubor parametrů, které definují, jak jsou poskytovány bezpečnostní služby pro konkrétní komunikační tok. SAD je úložiště, kde jsou tyto sady parametrů uloženy a spravovány pro všechny aktivní SA.

Každá položka v SAD odpovídá jedné SA a obsahuje komplexní sadu polí nezbytných pro zpracování zabezpečených paketů. Mezi klíčové součásti položky SAD patří: index bezpečnostních parametrů (Security Parameters Index – [SPI](/mobilnisite/slovnik/spi/)), jedinečný identifikátor SA; cílovou IP adresu (a často i zdrojovou adresu); kryptografické algoritmy, které mají být použity (např. [AES](/mobilnisite/slovnik/aes/) pro šifrování, SHA-256 pro integritu); konkrétní klíče pro tyto algoritmy; režim provozu (Transportní nebo Tunelový); životnost SA (v čase nebo zpracovaných bajtech); a parametry okna ochrany proti přehrání. Pro příchozí pakety přijímací uzel použije SPI a cílovou adresu k vyhledání správné položky v SAD, načte klíče a algoritmy a paket dešifruje a ověří. Pro odchozí pakety odesílající uzel konzultuje SAD, aby určil, jak paket před přenosem zašifrovat a zapouzdřit.

SAD funguje ve spojení s databází bezpečnostních politik (Security Policy Database – [SPD](/mobilnisite/slovnik/spd/)). SPD definuje pravidla politiky, která určují, *zda* má být provoz chráněn, a obecné požadavky na tuto ochranu. Když provoz odpovídá pravidlu SPD vyžadujícímu ochranu, systém buď použije existující SA (jejíž parametry jsou v SAD), nebo spustí vytvoření nové SA prostřednictvím protokolu pro správu klíčů, jako je IKEv2. Parametry nově vytvořené SA jsou následně instalovány do SAD. SAD je dynamicky aktualizována při vytváření, mazání nebo obnovování SA. Správa SAD je základní funkcí implementace IPsec, která zajišťuje dostupnost klíčů, sledování životností a odstranění zastaralých záznamů.

V sítích 3GPP je SAD nezbytná pro zabezpečení rozhraní, jako je N3 a N9 v 5G pomocí IPsec, nebo pro zabezpečení tunelů mezi UE a sítí ve scénářích jako je integrace WLAN. Umožňuje síti udržovat současně bezpečné asociace pro miliony zařízení, každou s vlastním kryptografickým kontextem. Robustnost a výkon implementace SAD přímo ovlivňují bezpečnost a škálovatelnost mobilní páteřní sítě.

## K čemu slouží

Databáze bezpečnostních asociací existuje proto, aby řešila problém správy komplexních, stavových parametrů vyžadovaných pro kryptografickou ochranu komunikací. Rané zabezpečené komunikace často používaly statické, předem sdílené klíče pro celé spoje, což bylo pro rozsáhlé, dynamické sítě nepružné a nejisté. Jak se protokoly jako IPsec vyvíjely, aby poskytovaly zabezpečení na úrovni toku nebo relace s dynamickým navazováním klíčů, byl potřebný mechanismus pro ukládání a načítání množství parametrů pro každý aktivní bezpečnostní kontext.

SAD byla vytvořena jako součást architektury IPsec (definované v IETF RFC) pro poskytnutí tohoto stavového úložiště. Bez SAD by bezpečnostní brána neměla efektivní způsob, jak spojit příchozí zabezpečené pakety se správnými dešifrovacími klíči a algoritmy, což by činilo IPsec nepoužitelným pro více současných spojení. Řeší tak omezení dřívějších ad-hoc bezpečnostních implementací, které nebyly škálovatelné. SAD spolu se SPD poskytuje strukturovaný, databází řízený přístup k vynucování bezpečnostních politik.

V rámci 3GPP se přijetí IPsec pro ochranu rozhraní páteřní sítě (např. mezi síťovými funkcemi) a tunelů uživatelských dat stalo klíčovým s přechodem na plně IP architektury a později na cloud-nativní jádra 5G. Koncept SAD je nedílnou součástí specifikací definujících zabezpečení pro rozhraní jako GTP-U, N3, N9 a pro přístup UE přes nedůvěryhodné sítě. Jeho účelem v 3GPP je umožnit standardizovanou, škálovatelnou a bezpečnou IP komunikaci v celém mobilním ekosystému, což zajišťuje, že každý zabezpečený tok má svůj vyhrazený kryptografický stav spolehlivě spravovaný síťovými prvky.

## Klíčové vlastnosti

- Ukládá parametry aktivních bezpečnostních asociací (SPI, klíče, algoritmy, životnosti)
- Indexována pomocí indexu bezpečnostních parametrů (SPI) a cílové adresy pro rychlé vyhledávání
- Používá se jak pro zpracování příchozích paketů (dešifrování/ověření), tak odchozích (šifrování)
- Dynamicky aktualizována protokoly pro správu klíčů, jako je IKEv2
- Nedílná součást implementace IPsec v branách a bezpečnostních funkcích 3GPP
- Umožňuje současnou správu tisíců až milionů odlišných bezpečnostních kontextů

## Související pojmy

- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)
- [SPD – Security Policy Database](/mobilnisite/slovnik/spd/)
- [SPI – Service Provider Identification](/mobilnisite/slovnik/spi/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.441** (Rel-19) — EVS Audio Processing Introduction
- **TS 26.442** (Rel-19) — EVS Codec Fixed Point ANSI-C Code
- **TS 26.443** (Rel-19) — EVS Codec Floating-Point C Code
- **TS 26.444** (Rel-19) — EVS Codec Conformance Test Sequences
- **TS 26.450** (Rel-19) — EVS Codec DTX System Level Aspects
- **TS 26.451** (Rel-19) — EVS Codec Voice Activity Detector (VAD) Specification
- **TS 26.452** (Rel-19) — EVS Codec Fixed-Point C Code Implementation
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TS 29.204** (Rel-19) — SS7 Security Gateway Functional Description
- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks

---

📖 **Anglický originál a plná specifikace:** [SAD na 3GPP Explorer](https://3gpp-explorer.com/glossary/sad/)
