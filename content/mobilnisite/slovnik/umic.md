---
slug: "umic"
url: "/mobilnisite/slovnik/umic/"
type: "slovnik"
title: "UMIC – User Plane Node Management Information Container"
date: 2025-01-01
abbr: "UMIC"
fullName: "User Plane Node Management Information Container"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/umic/"
summary: "User Plane Node Management Information Container (UMIC, kontejner informací o správě uzlu uživatelské roviny) je datová struktura zavedená v 5G pro přenos informací souvisejících se správou mezi funkc"
---

UMIC je datová struktura 5G, která přenáší informace o správě uzlů uživatelské roviny, jako je zatížení a stav zdrojů, mezi řídicími a uživatelskými funkcemi prostřednictvím PFCP relací.

## Popis

User Plane Node Management Information Container (UMIC, kontejner informací o správě uzlu uživatelské roviny) je koncept a datová struktura definovaná v architektuře 5G jádra sítě, konkrétně související s Packet Forwarding Control Protocol ([PFCP](/mobilnisite/slovnik/pfcp/)), který se používá pro komunikaci mezi funkcí řídicí roviny (CPF) – jako je Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) – a funkcí uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)). UMIC není samostatný protokol, ale kontejner nebo informační prvek, který může být zahrnut v určitých zprávách PFCP. Jeho hlavním účelem je přenos informací o správě a provozu týkajících se stavu UPF do řídicí CPF.

Architektonicky je UMIC generován UPF. Zapouzdřuje různé typy řídicích informací, které odrážejí aktuální provozní stav UPF. Tyto informace mohou zahrnovat metriky týkající se zatížení (např. využití [CPU](/mobilnisite/slovnik/cpu/), využití paměti, rychlost zpracování paketů), indikátory řízení přetížení (signalizující, že UPF se blíží nebo je ve stavu přetížení) a další řídicí data specifická pro uzel. UPF zahrnuje tento UMIC do zpráv PFCP odesílaných SMF, například v odpovědích na změnu PFCP relace nebo potenciálně v aktualizačních zprávách přidružení PFCP. Po přijetí zprávy obsahující UMIC SMF analyzuje kontejner, aby extrahovala řídicí informace.

Úlohou UMIC je poskytnout řídicí rovině viditelnost stavu a kapacity uzlů uživatelské roviny v reálném nebo téměř reálném čase. To umožňuje několik pokročilých funkcí správy sítě. Například SMF přijímající UMIC indikující vysoké zatížení konkrétní UPF může činit informovaná rozhodnutí pro nové relace, případně vybrat pro zřízení relace jinou, méně zatíženou UPF (vyrovnávání zatížení). Pokud UMIC signalizuje stav přetížení, SMF může spustit procedury řízení přetížení, jako je odmítnutí nových požadavků na relaci nebo plynulé přesměrování provozu. UMIC usnadňuje systém řízení s uzavřenou smyčkou, kde se řídicí rovina může dynamicky přizpůsobovat svým rozhodnutím na základě skutečného stavu zdrojů uživatelské roviny, což přesahuje statickou konfiguraci. To je klíčový prvek pro automatizaci sítě, elasticitu a efektivní využití zdrojů v cloud-nativních 5G jádrech sítě.

## K čemu slouží

UMIC byl zaveden v 5G Release 17, aby řešil potřebu vylepšené a dynamické správy disagregované uživatelské roviny. V předchozích architekturách a raných vydáních 5G byla rozhodnutí řídicí roviny (jako výběr [UPF](/mobilnisite/slovnik/upf/)) často založena na statické konfiguraci (např. profilech v Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/))) nebo jednoduchých politikách. Nebyl standardizovaný, v-pásmový mechanismus, kterým by UPF mohla proaktivně hlásit své dynamické zatížení nebo stav přetížení [SMF](/mobilnisite/slovnik/smf/) během aktivních [PFCP](/mobilnisite/slovnik/pfcp/) relací. Toto omezení mohlo vést k suboptimální distribuci zatížení, kdy SMF mohla pokračovat v přiřazování relací přetížené UPF, protože jí chyběly informace v reálném čase.

Vytvoření UMIC tento problém řeší definováním standardizovaného kontejneru pro přenos těchto zásadních řídicích informací v rámci existujícího signalizačního kanálu PFCP. To umožňuje okamžité a kontextově citlivé reakce řídicí roviny. Motivace vychází z cloud-nativních principů 5G, kde se předpokládá, že UPF budou softwarové instance škálované elasticky. Pro automatizaci škálování a směrování provozu vyžaduje řídicí rovina podrobné zpětné vazby od uživatelské roviny. UMIC poskytuje tuto zpětnovazební smyčku, umožňuje inteligentnější vyrovnávání zatížení, proaktivní vyhýbání se přetížení a zlepšenou celkovou odolnost sítě a kvalitu služeb. Představuje vývoj směrem k samooptimalizujícím se sítím, kde mohou funkce jádra sítě autonomně reagovat na měnící se podmínky zatížení.

## Klíčové vlastnosti

- Standardizovaný kontejner pro řídicí informace UPF v rámci signalizace PFCP
- Přenáší dynamické metriky zatížení (např. CPU, paměť, propustnost) z UPF do SMF
- Komunikuje stav přetížení a spouštěče pro akce řídicí roviny
- Umožňuje SMF dynamické, reálné vyrovnávání zatížení a výběr UPF
- Podporuje automatizaci s uzavřenou smyčkou a elastické škálování v cloud-nativních 5G jádrech
- Zvyšuje odolnost sítě a QoS tím, že předchází přetížení UPF

## Související pojmy

- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3

---

📖 **Anglický originál a plná specifikace:** [UMIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/umic/)
