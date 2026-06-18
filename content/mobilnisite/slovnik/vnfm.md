---
slug: "vnfm"
url: "/mobilnisite/slovnik/vnfm/"
type: "slovnik"
title: "VNFM – Virtualized Network Function Manager"
date: 2025-01-01
abbr: "VNFM"
fullName: "Virtualized Network Function Manager"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/vnfm/"
summary: "Virtualized Network Function Manager (VNFM) je funkční blok odpovědný za správu životního cyklu virtualizovaných síťových funkcí (VNF). Zpracovává instanciaci, škálování, aktualizace, ozdravování a uk"
---

VNFM je funkční blok v rámci architektury NFV MANO odpovědný za správu životního cyklu instancí virtualizovaných síťových funkcí (VNF), zahrnující jejich instanciaci, škálování, aktualizaci, ozdravování a ukončování.

## Popis

Virtualized Network Function Manager (VNFM) je klíčová entita v architektuře [NFV](/mobilnisite/slovnik/nfv/) Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)), definované [ETSI](/mobilnisite/slovnik/etsi/) a standardizované 3GPP pro telekomunikační prostředí. Jejím hlavním úkolem je kompletní správa životního cyklu jedné či více instancí virtualizované síťové funkce ([VNF](/mobilnisite/slovnik/vnf/)). VNFM pracuje na základě informací o nasazení a konfiguraci uvedených v popisu VNF (VNFD) a přijímá instrukce od nadřazeného orchestračního prvku, typicky NFV Orchestratoru ([NFVO](/mobilnisite/slovnik/nfvo/)).

Správa životního cyklu zahrnuje několik klíčových procedur. Pro instanciaci VNFM interpretuje VNFD, žádá o prostředky od [NFVI](/mobilnisite/slovnik/nfvi/) a koordinuje nasazení a konfiguraci jednotlivých komponent VNF ([VNFC](/mobilnisite/slovnik/vnfc/)). Pro škálování může VNFM provádět horizontální škálování (přidávání/odebírání instancí VNFC) nebo vertikální škálování (úpravu prostředků stávajících VNFC) na základě spouštěčů z politik nebo přímých požadavků. Dále spravuje softwarové aktualizace a upgrady instancí VNF s cílem minimalizovat dopad na služby. VNFM také provádí ozdravovací operace monitorováním stavu instancí VNF a automatickým zotavením z poruch, například opětovnou instanciací vadného VNFC.

VNFM vystavuje severovýchodní rozhraní, primárně směrem k NFVO, pro přijímání pokynů ke správě životního cyklu a poskytování notifikací. Klíčovým rozhraním je referenční bod Ve-Vnfm-em, používaný pro správu životního cyklu VNF. Má také jihozápadní rozhraní pro komunikaci s instancemi VNF samotnými (často využívající proprietární rozhraní pro správu prvků) a s Virtualized Infrastructure Managerem ([VIM](/mobilnisite/slovnik/vim/)) pro správu podkladových výpočetních, úložných a síťových prostředků. VNFM udržuje stavové informace pro každou spravovanou instanci VNF, což je nezbytné pro konzistentní operace.

V praktických nasazeních může být VNFM generický, spravující široké spektrum typů VNF od různých dodavatelů, nebo specifický pro konkrétní VNF či dodavatele. Tato volba ovlivňuje interoperabilitu a podporu funkcí. Role VNFM je klíčová pro automatizaci síťových operací, umožnění provisioning bez zásahu obsluhy a zajištění vysoké dostupnosti a elasticity vyžadované moderními cloud-nativními 5G jádry sítě a síťovými řezy.

## K čemu slouží

VNFM byl vytvořen k řešení provozní složitosti zavedené virtualizací síťových funkcí. Samotné běžení síťového softwaru na komerčním hardwaru (COTS) bylo nedostatečné; byl potřebný nový paradigmat managementu. Tradiční systémy pro správu síťových prvků (EMS) byly navrženy pro fyzické zařízení a nedokázaly zvládnout dynamickou povahu virtualizovaných prostředků, jako je instanciace na požádání, elastické škálování a automatizované zotavení.

VNFM to řeší tím, že poskytuje standardizovaného, automatizovaného správce pro softwarový životní cyklus VNF. Abstrahuje složitost podkladové virtualizované infrastruktury, což umožňuje síťovému orchestrátoru vydávat příkazy založené na záměru (např. "škáluj tuto VNF") bez nutnosti znát specifika hypervizoru nebo cloudové platformy. Toto oddělení zájmů je základním kamenem architektury NFV MANO, umožňuje multivendorovou interoperabilitu a brání uzamčení u konkrétního dodavatele na úrovni infrastruktury.

Historicky, bez VNFM, museli operátoři ručně zřizovat virtuální stroje, instalovat VNF software a konfigurovat připojení – proces, který mohl trvat dny nebo týdny. VNFM tyto úlohy automatizuje, čímž se doba zřizování zkracuje na minuty. Tato agilita není jen provozním zlepšením; je to obchodní faktor umožňující nové zdroje příjmů, jako jsou síťové řezy, kde musí být vyhrazené virtuální sítě vytvářeny a upravovány rychle pro různé zákazníky nebo služby. VNFM je tedy nezbytný pro transformaci telekomunikačních sítí na agilní, softwarově řízené platformy.

## Klíčové vlastnosti

- Orchestruje celý životní cyklus instancí VNF (instanciaci, škálování, aktualizace, ukončení)
- Provádí horizontální a vertikální škálování na základě politik nebo požadavků orchestračního prvku
- Provádí procedury obnovy z poruch a ozdravování pro VNF a jejich komponenty
- Interpretuje a provádí pokyny od NFV Orchestratoru (NFVO)
- Spravuje softwarové aktualizace a upgrady VNF s minimálním dopadem na službu
- Udržuje stavové a konfigurační informace pro spravované instance VNF

## Související pojmy

- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)
- [NFVO – Network Functions Virtualization Orchestrator](/mobilnisite/slovnik/nfvo/)
- [VIM – Virtualized Infrastructure Manager](/mobilnisite/slovnik/vim/)
- [VNF – Virtualized Network Function](/mobilnisite/slovnik/vnf/)
- [VNFC – Virtualized Network Function Component](/mobilnisite/slovnik/vnfc/)

## Definující specifikace

- **TS 28.311** (Rel-19) — Policy Management for 4G Networks
- **TS 28.500** (Rel-19) — Management of Virtualized Network Functions
- **TR 28.834** (Rel-18) — Technical Report
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 32.409** (Rel-19) — IMS Performance Management Measurements
- **TS 32.426** (Rel-19) — EPC Performance Measurements Specification
- **TS 32.842** (Rel-13) — Management of Virtualized 3GPP Core Networks
- **TR 33.818** (Rel-17) — SECAM/SCAS for 3GPP Virtualised Network Products
- **TR 33.927** (Rel-19) — Security Assurance for Virtualized Network Products

---

📖 **Anglický originál a plná specifikace:** [VNFM na 3GPP Explorer](https://3gpp-explorer.com/glossary/vnfm/)
