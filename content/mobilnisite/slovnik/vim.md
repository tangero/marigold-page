---
slug: "vim"
url: "/mobilnisite/slovnik/vim/"
type: "slovnik"
title: "VIM – Virtualized Infrastructure Manager"
date: 2025-01-01
abbr: "VIM"
fullName: "Virtualized Infrastructure Manager"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/vim/"
summary: "Virtualized Infrastructure Manager (VIM) je klíčová komponenta v architektuře NFV, která řídí a spravuje NFVI (infrastrukturu pro virtualizaci síťových funkcí). Je zodpovědný za orchestraci výpočetníc"
---

VIM je komponenta v architektuře NFV, která řídí a spravuje NFVI a orchestruje výpočetní, úložné a síťové zdroje, aby umožnila správu životního cyklu virtualizovaných síťových funkcí.

## Popis

Virtualized Infrastructure Manager (VIM) je základní funkční blok v architektonickém rámci [ETSI](/mobilnisite/slovnik/etsi/) [NFV](/mobilnisite/slovnik/nfv/) (Network Functions Virtualization), který byl přijat a rozšířen 3GPP pro správu virtualizovaných síťových zdrojů. Primární rolí VIM je dohled nad infrastrukturou NFV ([NFVI](/mobilnisite/slovnik/nfvi/)), která zahrnuje fyzický výpočetní, úložný a síťový hardware spolu s vrstvou hypervizoru nebo kontejnerizace (virtualizační vrstva). Funguje jako centralizovaný kontrolér pro jednu doménu infrastruktury, typicky datové centrum nebo místo připojení.

Operačně VIM pracuje tak, že zpřístupňuje sadu northbound [API](/mobilnisite/slovnik/api/) (často založených na OpenStack nebo jiných platformách pro správu cloudu), aby přijímal instrukce od NFV Orchestrátoru ([NFVO](/mobilnisite/slovnik/nfvo/)). Tyto instrukce zahrnují požadavky na alokaci zdrojů, instanciaci virtualizovaných síťových funkcí ([VNF](/mobilnisite/slovnik/vnf/)) a správu jejich životního cyklu. VIM překládá tyto vysokourovňové požadavky na konkrétní příkazy pro podkladovou infrastrukturu. Spravuje inventář dostupných fyzických a virtuálních zdrojů, zajišťuje provisioning virtuálních strojů nebo kontejnerů, alokuje virtuální sítě a úložiště a monitoruje stav a výkon infrastruktury. Mezi klíčové úkoly patří správa imagí (ukládání softwarových imagí VNF), správa katalogu zdrojů, správa chyb a výkonu NFVI a sběr záznamů o využití pro účely fakturace nebo účtování nákladů.

V kontextu 3GPP je VIM integrován do širšího rámce Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)). Zatímco 3GPP nestandardizuje samotnou implementaci VIM, definuje požadavky a rozhraní (jako referenční bod Or-Vi mezi NFVO a VIM), aby zajistil interoperabilitu. VIM je zásadní pro umožnění cloud-nativních principů v telekomunikačních sítích, což umožňuje nasazování síťových funkcí, jako je vEPC nebo vIMS, jako softwaru na komerčním hardwaru ([COTS](/mobilnisite/slovnik/cots/)). Poskytuje telekomunikační doméně agilitu a efektivitu cloud computingu, podporuje elastické škálování, rychlé nasazování služeb a optimalizované využití zdrojů.

## K čemu slouží

VIM byl vytvořen, aby řešil základní výzvu správy složitých, disagregovaných hardwarových zdrojů v prostředí NFV. Tradiční telekomunikační sítě používaly pro každou síťovou funkci těsně integrovaná proprietární hardwarová zařízení. Přechod na NFV odděluje software od hardwaru, ale to vyžaduje novou vrstvu správy pro dynamické sdružování, alokaci a řízení výpočetních, úložných a síťových zdrojů standardizovaným způsobem.

Před NFV a konceptem VIM vyžadovalo nasazení nové síťové služby pořízení, instalaci a propojení fyzických zařízení – proces trvající měsíce. VIM jako součást stacku MANO umožňuje tento proces automatizovat a řídit softwarově, čímž se doba nasazení zkrátí na minuty. Řeší problém izolovaných zdrojů a nízkého využití implementací cloudového modelu sdílené infrastruktury. To dramaticky zvyšuje provozní efektivitu a agilitu a umožňuje operátorům rychle uvádět nové služby a škálovat je na požádání podle vzorců provozu.

Z pohledu 3GPP bylo přijetí VIM a rámce NFV motivováno potřebou podpory sítí 5G a budoucích sítí. Požadavky 5G na síťové slicing, ultra-nízkou latenci a masivní škálování jsou ekonomicky a technicky náročné s tradičním hardwarem. VIM poskytuje základní mechanismus řízení zdrojů, který umožňuje síťový slicing – vytvářením izolovaných sad virtuálních zdrojů ze sdíleného fyzického fonde pro každý slice. Jeho vytvoření bylo nezbytným krokem v transformaci telekomunikačních sítí na flexibilní, softwarově definované platformy schopné podporovat rozmanité případy užití 5G.

## Klíčové vlastnosti

- Spravuje a řídí zdroje NFVI (výpočetní, úložné, síťové) v rámci domény infrastruktury.
- Orchestruje životní cyklus virtuálních zdrojů (VM, kontejnery, sítě) pro nasazení VNF.
- Udržuje inventář dostupných a alokovaných fyzických a virtuálních zdrojů.
- Sbírá informace o chybách a výkonu z NFVI pro monitorování a zajištění služeb.
- Zpřístupňuje northbound rozhraní (např. Or-Vi) pro NFV Orchestrátor pro přijímání požadavků na provisioning zdrojů.
- Spravuje softwarové image pro VNF a zajišťuje funkčnost katalogu zdrojů.

## Související pojmy

- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [NFVI – Network Functions Virtualization Infrastructure](/mobilnisite/slovnik/nfvi/)
- [NFVO – Network Functions Virtualization Orchestrator](/mobilnisite/slovnik/nfvo/)
- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)
- [VNF – Virtualized Network Function](/mobilnisite/slovnik/vnf/)

## Definující specifikace

- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 28.311** (Rel-19) — Policy Management for 4G Networks
- **TS 28.500** (Rel-19) — Management of Virtualized Network Functions
- **TS 32.842** (Rel-13) — Management of Virtualized 3GPP Core Networks
- **TR 33.818** (Rel-17) — SECAM/SCAS for 3GPP Virtualised Network Products
- **TR 33.927** (Rel-19) — Security Assurance for Virtualized Network Products

---

📖 **Anglický originál a plná specifikace:** [VIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/vim/)
