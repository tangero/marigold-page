---
slug: "nfvo"
url: "/mobilnisite/slovnik/nfvo/"
type: "slovnik"
title: "NFVO – Network Functions Virtualization Orchestrator"
date: 2025-01-01
abbr: "NFVO"
fullName: "Network Functions Virtualization Orchestrator"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nfvo/"
summary: "Centrální entita pro řízení a orchestraci v síti založené na NFV. Automatizuje životní cyklus síťových služeb (složených z více VNF) a spravuje jejich prostředky v rámci NFVI. Je klíčová pro agilitu s"
---

NFVO je centrální entita pro řízení a orchestraci, která automatizuje životní cyklus síťových služeb a spravuje jejich prostředky v rámci infrastruktury NFV.

## Popis

Network Functions Virtualization Orchestrator (NFVO) je mozkem architektury [NFV](/mobilnisite/slovnik/nfv/) Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)). Jeho primární funkcí je orchestrace síťových služeb (NS) a správa prostředků [NFVI](/mobilnisite/slovnik/nfvi/) napříč více doménami a lokalitami. Síťová služba je kompletní, end-to-end řetězec služeb složený z jedné nebo více Virtualized Network Functions (VNF) a virtuálních spojů, které je propojují. NFVO automatizuje celý životní cyklus těchto služeb – včetně instanciace, škálování, aktualizace, hojení a ukončení – přičemž překládá služební šablony vysoké úrovně na proveditelné příkazy pro nasazení a konfiguraci.

Architektonicky NFVO pracuje na vyšší úrovni než Virtualized Infrastructure Manager (VIM). Zatímco VIM spravuje virtuální prostředky v rámci jedné domény NFVI, NFVO má globální pohled. Komunikuje s jedním nebo více VIMy, aby rezervoval a alokoval prostředky z podkladových fondů NFVI. Také komunikuje s jedním nebo více VNF Managery (VNFM) pro zvládnutí životního cyklu jednotlivých instancí VNF. NFVO spravuje katalog síťových služeb (ukládá šablony NS) a katalog VNF (ukládá balíčky VNF), které definují šablony pro nasazení. Klíčová rozhraní zahrnují referenční bod Or-Vnfm k VNFM, Or-Vi k VIM a Os-Ma-nfvo pro integraci s [OSS](/mobilnisite/slovnik/oss/)/[BSS](/mobilnisite/slovnik/bss/).

Pracovní postup NFVO začíná přijetím požadavku na službu, často z Operations Support System (OSS). Ověří žádost vůči katalogu, provede kontrolu proveditelnosti prostředků napříč cílovými body přítomnosti (PoP) NFVI a vytvoří plán nasazení. Poté koordinuje proces: dá pokyn VIMům k přípravě rezervací prostředků, nasměruje VNFM k instanciaci a konfiguraci jednotlivých VNF a nakonec podle služební šablony zřídí virtuální síťové propojení mezi nimi. Nad rámec instanciace NFVO nepřetržitě monitoruje výkon a stav služby. Může spouštět automatizované akce škálování (out/in, up/down) na základě politik, koordinovat softwarové aktualizace napříč VNF a iniciovat procedury hojení (např. re-instanciaci) v případě selhání VNF.

V kontextu 3GPP je NFVO nedílnou součástí správy síťových řezů a služeb jádra 5G. Spolupracuje s dalšími systémy správy 3GPP, jako je Network Slice Management Function (NSMF) a Communication Service Management Function (CSMF), k realizaci komplexních end-to-end síťových řezů. Automatizací těchto procesů NFVO drasticky snižuje dobu nasazení služeb z měsíců na minuty, optimalizuje využití prostředků a umožňuje dynamické, politikami řízené síťové operace, které jsou nezbytné pro podporu různorodých případů užití 5G s různými požadavky na latenci, šířku pásma a spolehlivost.

## K čemu slouží

NFVO bylo vytvořeno k řešení provozní složitosti a manuální neefektivity spojené s nasazováním a správou kompozitních síťových služeb postavených z virtualizovaných funkcí. V raných nasazeních [NFV](/mobilnisite/slovnik/nfv/) vyžadovala instanciace a propojování VNF významnou manuální koordinaci mezi týmy spravujícími výpočetní, síťovou a aplikační vrstvu, což vedlo k pomalému zavádění služeb a vysoké chybovosti.

Jeho účelem je poskytnout automatizovanou, end-to-end služební orchestráci. Před NFVO mohli operátoři virtualizovat jednotlivé funkce (VNF), ale jejich spojování do fungující služby zůstávalo manuálním, náchylným k chybám procesem. NFVO toto spojování automatizuje a zachází se souborem VNF a jejich konektivitou jako s jedinou spravovatelnou entitou – síťovou službou. Tím řeší kritickou potřebu agility, která operátorům umožňuje rychle zavádět, upravovat nebo ukončovat služby v reakci na požadavky trhu.

Dále NFVO umožňuje efektivní správu prostředků v globálním měřítku. Dokáže činit optimální rozhodnutí o umístění VNF napříč distribuovanou cloudovou infrastrukturou (centrální, regionální, edge datová centra) s ohledem na omezení jako latence, dostupnost prostředků a náklady. To je klíčové pro nákladově efektivní síťové operace a pro splnění přísných požadavků na umístění vznikajících služeb, jako je mobilní edge computing a ultra-reliable low-latency communications (URLLC).

## Klíčové vlastnosti

- End-to-end správa životního cyklu síťových služeb (NS)
- Orchestrace napříč více VIMy a infrastrukturními doménami
- Automatizované škálování a hojení služeb založené na politikách
- Správa katalogů pro deskriptory (šablony) NS a VNF
- Globální inventář prostředků a správa rezervací
- Integrační bod pro OSS/BSS a vyšší správce řezů

## Související pojmy

- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [NFVI – Network Functions Virtualization Infrastructure](/mobilnisite/slovnik/nfvi/)
- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)

## Definující specifikace

- **TS 28.311** (Rel-19) — Policy Management for 4G Networks
- **TS 28.500** (Rel-19) — Management of Virtualized Network Functions
- **TR 28.834** (Rel-18) — Technical Report
- **TS 28.890** (Rel-16) — ONAP-3GPP 5G Management Compatibility Study
- **TS 32.842** (Rel-13) — Management of Virtualized 3GPP Core Networks
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TR 33.818** (Rel-17) — SECAM/SCAS for 3GPP Virtualised Network Products
- **TR 33.927** (Rel-19) — Security Assurance for Virtualized Network Products

---

📖 **Anglický originál a plná specifikace:** [NFVO na 3GPP Explorer](https://3gpp-explorer.com/glossary/nfvo/)
