---
slug: "vnf"
url: "/mobilnisite/slovnik/vnf/"
type: "slovnik"
title: "VNF – Virtualized Network Function"
date: 2026-01-01
abbr: "VNF"
fullName: "Virtualized Network Function"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/vnf/"
summary: "Virtualizovaná síťová funkce (VNF) je softwarová implementace tradičního síťového uzlu (jako MME, PGW), která běží na virtualizované infrastruktuře (cloudu). Je základním stavebním prvkem virtualizace"
---

VNF je softwarová implementace tradičního uzlu telekomunikační sítě, která běží na cloudové infrastruktuře a slouží jako základní stavební prvek virtualizace síťových funkcí.

## Popis

Virtualizovaná síťová funkce (VNF) je softwarová realizace síťové funkce, která byla tradičně implementována jako dedikovaný fyzický přístroj. V kontextu 3GPP a [ETSI](/mobilnisite/slovnik/etsi/) [NFV](/mobilnisite/slovnik/nfv/) je VNF nasaditelnou jednotkou funkcionality – jako například Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) nebo Session Border Controller (SBC) – která je zabalena jako software a může běžet na virtuálních strojích ([VM](/mobilnisite/slovnik/vm/)) nebo kontejnerech nad sdílenou, cloudové infrastruktuře podobnou infrastrukturou nazývanou NFV Infrastructure ([NFVI](/mobilnisite/slovnik/nfvi/)). Samotná VNF se skládá z jedné nebo více vnitřních komponent (VNF Components - VNFCs), které mohou být nasazeny na oddělených virtualizovaných zdrojích. Každá VNF má deskriptor (VNFD), který definuje její požadavky: výpočetní, úložné a síťové potřeby a chování správy životního cyklu.

Fungování VNF zahrnuje její instanciaci, konfiguraci a správu rámcem NFV Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)). Orchestrátor ([NFVO](/mobilnisite/slovnik/nfvo/)) používá VNFD k vyžádání alokace virtuálních zdrojů (z NFVI) prostřednictvím Virtualized Infrastructure Manager (VIM). Jakmile je vytvořeno virtuální prostředí (např. VM s konkrétním CPU, pamětí, síťovými rozhraními), je na něj nasazen softwarový image VNF. VNF Manager (VNFM) poté spravuje životní cyklus této konkrétní instance VNF: její spuštění, konfiguraci síťovými parametry (jako IP adresy, směrovací pravidla), její škálování (přidávání/odebírání VNFCs na základě zatížení), aktualizaci a ukončení. VNF vykonává svou zamýšlenou síťovou funkci (např. směrování paketů, správa relací) stejně jako by to dělal fyzický uzel, ale komunikuje přes virtuální sítě a používá abstrahované zdroje.

Klíčové komponenty v architektuře VNF zahrnují VNFCs, což jsou modulární softwarové procesy; interní managementové rozhraní VNF pro VNFM; a její externí funkční rozhraní, která se připojují k jiným VNF nebo fyzickým síťovým funkcím (PNFs) za účelem vytvoření servisního řetězce. Například VNF implementující funkci 5G Core Network (jako AMF) by měla rozhraní pro komunikaci s dalšími core VNFs (SMF, UPF) a RAN. Její role v síti je poskytovat stejnou telekomunikační službu jako hardwarová skříň, ale s agilitou softwaru: může být rychle nasazena, pružně škálována pro zvládnutí kolísání provozu a centrálně spravována, což drasticky snižuje náklady a zvyšuje provozní flexibilitu. Specifikace 3GPP, zejména v managementové doméně (např. TS 28.541, TS 28.545), definují požadavky a rozhraní pro VNFs jako součást celkové virtualizované síťové architektury.

## K čemu slouží

Koncept VNF existuje za účelem transformace telekomunikačních sítí z hardwarově orientovaných na softwarově orientované a řeší problémy vysokých nákladů, dlouhých cyklů nasazení a nepružnosti spojené s proprietárními fyzickými přístroji. Tradiční síťové uzly byly monolitické, vyžadovaly dedikovaný prostor, napájení a manuální konfiguraci. Škálování vyžadovalo nákup a instalaci dalších skříní. Tento model byl neudržitelný s explozí datového provozu a potřebou rychlé inovace služeb. Virtualizace, inspirovaná cloud computingem, motivovala vytvoření VNFs k oddělení síťových funkcí od hardwaru.

NFV, a tedy VNFs, byly vytvořeny k řešení těchto omezení tím, že umožňují síťovým funkcím běžet jako software na komerčních serverech standardní řady v datových centrech. Tím se snižují kapitálové výdaje (sdílený hardware) i provozní výdaje (automatizovaný management). Také umožňuje rychlejší zavádění nových služeb pouhým nasazením nového VNF softwaru. Pro 3GPP bylo přijetí VNFs (formalizované v Rel-13) hnací silou potřeby učinit core sítě (EPC, 5GC) agilnějšími a škálovatelnějšími pro podporu různorodých služeb jako IoT a network slicing. Umožňuje operátorům dynamicky alokovat zdroje tam, kde jsou potřeba, a zlepšovat tak efektivitu.

Historický kontext je takový, že telekomunikační průmysl, vedený ETSI's NFV ISG, začal tuto transformaci kolem roku 2012. 3GPP integrovalo tyto koncepty do svých managementových specifikací, aby zajistilo, že virtualizované 3GPP síťové funkce (jako ty v 5G Core) mohou být spravovány konzistentně. VNFs jsou základními enablery cloud-nativních sítí, podporujícími automatizaci, škálovatelnost a ekonomický model potřebný pro budoucí telekomunikační služby.

## Klíčové vlastnosti

- Softwarová implementace síťové funkce, nasaditelná na virtualizované infrastruktuře
- Definována deskriptorem VNF (VNFD) specifikujícím požadavky na zdroje a konektivitu
- Složena z jedné nebo více komponent VNF (VNFCs) pro modulární nasazení
- Životní cyklus spravován VNF Managerem (VNFM) (instance, škálování, ukončení)
- Může být pružně škálována (in/out, up/down) na základě zatížení a politik
- Propojuje se s dalšími VNFs/PNFs přes virtuální sítě za účelem poskytování end-to-end služeb

## Související pojmy

- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [NFVI – Network Functions Virtualization Infrastructure](/mobilnisite/slovnik/nfvi/)
- [NFVO – Network Functions Virtualization Orchestrator](/mobilnisite/slovnik/nfvo/)
- [VNFM – Virtualized Network Function Manager](/mobilnisite/slovnik/vnfm/)
- [VIM – Virtualized Infrastructure Manager](/mobilnisite/slovnik/vim/)

## Definující specifikace

- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.310** (Rel-19) — Energy Efficiency Management for 5G Networks
- **TS 28.311** (Rel-19) — Policy Management for 4G Networks
- **TS 28.500** (Rel-19) — Management of Virtualized Network Functions
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.545** (Rel-17) — Fault Supervision for 5G Networks
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.801** (Rel-15) — Management and Orchestration of Network Slicing
- **TR 28.834** (Rel-18) — Technical Report
- **TS 28.890** (Rel-16) — ONAP-3GPP 5G Management Compatibility Study
- **TS 32.842** (Rel-13) — Management of Virtualized 3GPP Core Networks
- **TR 32.972** (Rel-19) — Energy Efficiency Study for 5G Networks
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TR 33.818** (Rel-17) — SECAM/SCAS for 3GPP Virtualised Network Products
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [VNF na 3GPP Explorer](https://3gpp-explorer.com/glossary/vnf/)
