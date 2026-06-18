---
slug: "vm"
url: "/mobilnisite/slovnik/vm/"
type: "slovnik"
title: "VM – Virtual Machine"
date: 2025-01-01
abbr: "VM"
fullName: "Virtual Machine"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/vm/"
summary: "Softwarová emulace fyzického počítačového systému umožňující provádění síťových funkcí jako izolovaných softwarových instancí. Je základem pro virtualizaci síťových funkcí (NFV), která umožňuje flexib"
---

VM (virtuální stroj) je softwarová emulace fyzického počítačového systému, která provádí síťové funkce jako izolované instance, a tvoří tak základ pro virtualizaci síťových funkcí (NFV) umožňující flexibilní a škálovatelné telekomunikační služby.

## Popis

Virtuální stroj (VM) je softwarová abstrakce, která emuluje funkčnost fyzického počítače včetně jeho procesoru, paměti, úložiště a síťových rozhraní. Běží na hypervizoru (neboli monitoru virtuálních strojů) nainstalovaném na fyzickém serverovém hardwaru. Hypervizor přiděluje fyzické zdroje (výpočetní výkon, úložiště, síť) každému VM, čímž zajišťuje izolaci a zabezpečení mezi více VM běžícími na stejném hostiteli. Každý VM obsahuje vlastní hostovaný operační systém a aplikační software a z pohledu softwaru v něm běžícího se chová jako nezávislý fyzický stroj. Tato izolace je klíčovým architektonickým principem, který zabraňuje tomu, aby porucha nebo bezpečnostní incident v jednom VM ovlivnily ostatní na stejném hostiteli.

V kontextu sítí 3GPP jsou VM primárním prováděcím prostředím pro virtualizované síťové funkce ([VNF](/mobilnisite/slovnik/vnf/)). Funkce jádra sítě, jako je [MME](/mobilnisite/slovnik/mme/), [SGW](/mobilnisite/slovnik/sgw/), [PGW](/mobilnisite/slovnik/pgw/) a později [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/) a [UPF](/mobilnisite/slovnik/upf/) v 5GC, mohou být implementovány jako softwarové balíčky nasazené v rámci VM. Hypervizor spravuje životní cyklus těchto VM, včetně vytváření instancí, škálování, migrace a ukončování. Přidělování zdrojů je dynamické; hypervizor může na základě aktuální zátěže a požadavků na výkon VNF upravovat počet jader vCPU, paměť a šířku pásma virtuálního síťového rozhraní přiřazeného VM, což je schopnost řízená orchestrátorem [NFV](/mobilnisite/slovnik/nfv/) (NFVO).

Role VM je ústřední pro architektonický rámec ETSI NFV, který 3GPP přijímá a na který odkazuje. VM poskytuje nezbytnou izolaci a záruky zdrojů pro síťové funkce úrovně operátora (carrier-grade). Umožňuje operátorům nasazovat síťové služby na standardním hardwaru (COTS) v datových centrech, a odklonit se tak od proprietárních integrovaných zařízení. Tento posun umožňuje rychlou inovaci služeb, protože nové VNF lze vyvíjet a nasazovat jako softwarové aktualizace. Dále VM podporují vysokou dostupnost prostřednictvím živé migrace, kdy lze běžící VM s minimálním přerušením služby přesunout na jiný fyzický hostitel za účelem údržby nebo vyrovnávání zátěže.

## K čemu slouží

VM byl do specifikací 3GPP zaveden pro podporu celoprůmyslového přechodu k virtualizaci síťových funkcí (NFV). Před NFV byly telekomunikační sítě budovány pomocí monolitických, proprietárních hardwarových zařízení pro každou síťovou funkci (např. fyzický firewall, fyzický MME). Tento přístup vedl k dlouhým inovačním cyklům, vysokým kapitálovým a provozním nákladům, závislosti na dodavateli a neefektivnímu využívání zdrojů, protože každé zařízení bylo dimenzováno na špičkové zatížení a často zůstávalo nevyužité.

Účelem standardizace konceptu VM v rámci 3GPP bylo poskytnout společný, interoperabilní základ pro virtualizovaná nasazení. Řeší problém závislosti na hardwaru tím, že abstrahuje síťové funkce do softwaru, který může běžet na standardizované cloudové infrastruktuře. To umožňuje operátorům dosáhnout větší agility a pružně škálovat služby nahoru nebo dolů podle poptávky. Také usnadňuje prostředí s více dodavateli, protože VNF od různých dodavatelů mohou v zásadě běžet na stejné infrastruktuře NFV (NFVI), pokud jsou v souladu se specifikacemi a rozhraními VM.

Historicky tuto práci poháněly požadavky operátorů na snížení nákladů a provozní flexibilitu, což vedlo ke spolupráci mezi 3GPP a ETSI ISG NFV. Počáteční integrace ve verzi 10 (Release 10) označila začátek formální architektonické podpory pro virtualizaci a připravila cestu pro cloud-nativní vývoj viděný v pozdějších verzích s kontejnery a mikroslužbami.

## Klíčové vlastnosti

- Abstrakce hardwaru a izolace prostřednictvím hypervizoru
- Nezávislý hostovaný operační systém na VM
- Dynamické přidělování zdrojů (vCPU, paměť, úložiště)
- Podpora živé migrace mezi fyzickými hostiteli
- Výkon a bezpečnostní izolace úrovně operátora (carrier-grade)
- Standardizovaná rozhraní pro správu a orchestraci (např. prostřednictvím VIM)

## Související pojmy

- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [VNF – Virtualized Network Function](/mobilnisite/slovnik/vnf/)
- [NFVI – Network Functions Virtualization Infrastructure](/mobilnisite/slovnik/nfvi/)
- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 28.515** (Rel-19) — Fault Management for Virtualized Networks
- **TS 28.516** (Rel-19) — Fault Management for Virtualized Mobile Networks
- **TS 29.892** (Rel-16) — Study on User Plane Protocol in 5GC
- **TS 32.501** (Rel-19) — Self-Configuration of Network Elements Concepts
- **TS 32.842** (Rel-13) — Management of Virtualized 3GPP Core Networks
- **TR 33.818** (Rel-17) — SECAM/SCAS for 3GPP Virtualised Network Products
- **TR 33.848** (Rel-18) — Technical Report on Virtualisation Security
- **TR 33.927** (Rel-19) — Security Assurance for Virtualized Network Products

---

📖 **Anglický originál a plná specifikace:** [VM na 3GPP Explorer](https://3gpp-explorer.com/glossary/vm/)
