---
slug: "bng"
url: "/mobilnisite/slovnik/bng/"
type: "slovnik"
title: "BNG – Broadband Network Gateway"
date: 2025-01-01
abbr: "BNG"
fullName: "Broadband Network Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bng/"
summary: "Broadband Network Gateway (BNG) je síťový prvek, který agreguje provoz předplatitelů ze širokopásmových přístupových sítí a poskytuje IP konektivitu k jádrové síti. Slouží jako brána mezi přístupovými"
---

BNG (Broadband Network Gateway) je síťová brána, která agreguje provoz předplatitelů z širokopásmových přístupových sítí, aby poskytla IP konektivitu a správu předplatitelů pro jádrovou síť poskytovatele služeb.

## Popis

Broadband Network Gateway (BNG) funguje jako hlavní bod agregace a řízení v širokopásmových sítích, umístěný na hranici mezi přístupovými sítěmi a jádrovou IP sítí poskytovatele služeb. Architektonicky se skládá z několika klíčových komponent: modulu správy předplatitelů, který zajišťuje autentizaci, autorizaci a účtování ([AAA](/mobilnisite/slovnik/aaa/)) pomocí protokolů jako RADIUS nebo Diameter; funkce vynucování politik, která aplikuje servisní politiky a pravidla kvality služeb (QoS); směrovacího modulu, který spravuje IP směrování mezi přístupovými a jádrovými sítěmi; a systému řízení provozu, který zajišťuje tvarování provozu, policování a přidělování šířky pásma. BNG vytváří a udržuje relace předplatitelů, typicky využívaje správu relací pomocí PPP (Point-to-Point Protocol) nebo IPoE (IP over Ethernet), a přiděluje předplatitelům IP adresy buď lokálně, nebo prostřednictvím externích [DHCP](/mobilnisite/slovnik/dhcp/) serverů.

Při provozu, když se předplatitel připojí k síti, BNG jej autentizuje proti databázi předplatitelů, nastaví odpovídající servisní profil a aplikuje konfigurované politiky pro danou úroveň služeb předplatitele. Spravuje celý životní cyklus relace předplatitele, od počátečního připojení přes využívání služeb až po odpojení. BNG implementuje hierarchickou QoS (H-QoS), aby zajistila, že provoz od více předplatitelů sdílejících stejnou fyzickou infrastrukturu obdrží odpovídající přidělení šířky pásma podle jejich smluv o úrovni služeb (SLA). Také provádí klasifikaci a značkování provozu, aplikuje hodnoty Differentiated Services Code Point ([DSCP](/mobilnisite/slovnik/dscp/)) na pakety, aby umožnila end-to-end QoS v celé síti.

Role BNG přesahuje základní konektivitu a zahrnuje pokročilé služby, jako je distribuce multicastového videa, kde funguje jako replikační bod multicastu pro [IPTV](/mobilnisite/slovnik/iptv/) služby, implementuje funkce [IGMP](/mobilnisite/slovnik/igmp/)/[MLD](/mobilnisite/slovnik/mld/) snoopingu a proxy. Poskytuje bezpečnostní funkce včetně izolace předplatitelů, prevence útoků a možnosti zákonného odposlechu podle požadavků regulatorních rámců. Pro síťovou redundanci a škálovatelnost BNG často pracují v konfiguraci active-standby nebo active-active za použití protokolů jako VRRP (Virtual Router Redundancy Protocol) nebo proprietárních clusteringových mechanismů. BNG rozhraní s různými síťovými prvky: směrem k jádrové síti přes IP/[MPLS](/mobilnisite/slovnik/mpls/) rozhraní, směrem k přístupovým uzlům (DSLAM, OLT, CMTS) a k podpůrným systémům, jako jsou policy servery, fakturační systémy a platformy pro správu sítě.

Moderní implementace BNG podporují virtualizaci a cloudové architektury, což jim umožňuje běžet jako virtuální síťové funkce (VNF) na komerčním hardwaru standardní dostupnosti. Tento vývoj umožňuje flexibilnější modely nasazení a lepší integraci s kontroléry softwarově definovaných sítí (SDN). BNG také hraje klíčovou roli v konvergenčních scénářích, podporuje jak pevný, tak mobilní širokopásmový přístup prostřednictvím společných rámců pro správu předplatitelů a vynucování politik, což je obzvláště důležité pro operátory nabízející multi-play služby.

## K čemu slouží

BNG byla vytvořena, aby řešila omezení dřívějších řešení pro agregaci širokopásmových služeb, která nedokázala škálovat na podporu milionů předplatitelů s různorodými požadavky na služby. Před standardizovanými architekturami BNG používali poskytovatelé služeb různé proprietární brány a směrovače s omezenými možnostmi správy předplatitelů, což ztěžovalo nabízet diferencované služby, implementovat konzistentní politiky nebo ekonomicky škálovat. Rozšíření širokopásmového internetového přístupu na počátku 21. století vytvořilo poptávku po standardizovaném přístupu k agregaci předplatitelů, který by podporoval nejen základní přístup k internetu, ale také hlasové, video a obchodní služby přes stejnou infrastrukturu.

Hlavní problémy, které BNG řeší, zahrnují: poskytnutí škálovatelné architektury pro správu relací předplatitelů, která zvládne miliony souběžných relací; umožnění diferenciace služeb pomocí sofistikovaného vynucování politik a mechanismů QoS; podporu více přístupových technologií ([DSL](/mobilnisite/slovnik/dsl/), optika, kabel, bezdrátové) prostřednictvím společné agregační platformy; a usnadnění konvergence mezi pevnými a mobilními sítěmi. Architektura BNG umožňuje poskytovatelům služeb přejít od jednoduchého best-effort internetového přístupu k řízeným službám se zaručenými výkonnostními charakteristikami, což je nezbytné pro ziskové poskytování triple-play a quad-play služeb.

Historicky byl vývoj standardů BNG v rámci 3GPP a dalších standardizačních orgánů hnán potřebou interoperability mezi zařízeními od různých dodavatelů a požadavkem na konzistentní poskytování služeb napříč rozsáhlými geografickými oblastmi. Koncept BNG se vyvinul z dřívějších implementací broadband remote access server (BRAS), s vylepšenými schopnostmi pro řízení politik, QoS a integrací s IMS (IP Multimedia Subsystem) pro multimediální služby. Její standardizace v releasech 3GPP umožnila těsnější integraci s mobilními sítěmi, podporu konvergence pevných a mobilních sítí a připravila cestu pro jednotnou správu předplatitelů napříč různými přístupovými technologiemi.

## Klíčové vlastnosti

- Správa relací předplatitelů s podporou PPP a IPoE
- Hierarchická QoS (H-QoS) s více servisními úrovněmi a tvarováním provozu
- Vynucování politik prostřednictvím integrace s PCRF/PCF
- Multicastová replikace pro IPTV a video služby
- Integrace AAA se servery RADIUS/Diameter
- Možnosti zákonného odposlechu pro regulatorní shodu

## Související pojmy

- [AAA – Authentication, Authorization, and Accounting](/mobilnisite/slovnik/aaa/)
- [BRAS – Broadband Remote Access Server](/mobilnisite/slovnik/bras/)

## Definující specifikace

- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.839** (Rel-12) — Fixed-Mobile Convergence Architecture Study
- **TS 23.896** (Rel-12) — Policy & Charging Control for Fixed Broadband Convergence
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study

---

📖 **Anglický originál a plná specifikace:** [BNG na 3GPP Explorer](https://3gpp-explorer.com/glossary/bng/)
