---
slug: "dsr"
url: "/mobilnisite/slovnik/dsr/"
type: "slovnik"
title: "DSR – Distributed Speech Recognition"
date: 2025-01-01
abbr: "DSR"
fullName: "Distributed Speech Recognition"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dsr/"
summary: "Servisní architektura, ve které je zpracování rozpoznávání řeči rozděleno mezi mobilní zařízení (front-end) a síťový server (back-end). Zařízení extrahuje a komprimuje řečové příznaky, které jsou přen"
---

DSR je servisní architektura pro mobilní sítě, ve které je rozpoznávání řeči rozděleno mezi zařízení, které extrahuje a komprimuje řečové příznaky, a síťový server, který provádí finální rozpoznání.

## Popis

Distributed Speech Recognition (DSR) je architektura typu klient-server navržená k poskytování přesných služeb rozpoznávání řeči přes mobilní sítě. Funguje tak, že rozděluje úlohu rozpoznání mezi uživatelské zařízení (UE) a vzdálený rozpoznávací server v síti. UE provádí 'front-end' zpracování: zachytí zvuk pomocí mikrofonu, aplikuje akustické předzpracování (potlačení šumu, eliminace ozvěny) a následně extrahuje sadu kompaktních parametrických reprezentací (příznaků) řečového signálu, typicky Mel-Frequency Cepstral Coefficients (MFCC). Tyto příznaky jsou pak zakódovány pomocí standardizovaného, bitově efektivního kodeku a přeneseny přes datový kanál do sítě.

V síti přijímá proud příznaků vyhrazený DSR server. Tento server hostuje 'back-end' rozpoznávací engine, který zahrnuje akustické modely, výslovnostní slovníky a jazykové modely. Server dekóduje proud příznaků a používá statistické porovnávání vzorů (jako Hidden Markovovy modely nebo hluboké neuronové sítě) k převedení příznaků na textový řetězec nebo sémantický příkaz. Výsledek je pak odeslán zpět k UE nebo na jiný aplikační server. Toto oddělení je klíčové; umožňuje, aby výpočetně náročné a paměťově nákladné modelovací a vyhledávací procesy zůstaly na výkonných, aktualizovatelných serverech, zatímco UE zvládá lehčí, standardizovaný front-end.

Úlohou DSR je poskytovat konzistentní, vysoce přesný rozpoznávací zážitek nezávislý na výpočetním výkonu UE a proměnlivé kvalitě zvukového kanálu. Přenosem pouze příznaků (několik kbps) namísto plného zvukového proudu (např. 64 kbps pro [PCM](/mobilnisite/slovnik/pcm/)) šetří šířku pásma a je odolnější vůči přenosovým chybám a zkreslením od nízkobitových hlasových kodeků, která by degradovala rozpoznávání na straně serveru, pokud by byla aplikována na dekódovaný zvuk. Je to služební enabler pro síťové hlasové asistenty, automatické hlasové vytáčení a hlasem ovládané služby ve vozidlech.

## K čemu slouží

DSR bylo vytvořeno k vyřešení problému poskytování vysoce kvalitního, serverového rozpoznávání řeči ve variabilním a někdy omezeném prostředí raných mobilních sítí (2G, 3G). Tradiční 'pouze serverové' rozpoznávání, kdy UE odesílá komprimovaný zvuk (např. pomocí [AMR](/mobilnisite/slovnik/amr/)), trpělo tím, že hlasové kodeky byly optimalizovány pro lidský sluch, nikoli pro strojové rozpoznávání. Artefakty kodeků a přenosové chyby mohly významně snížit přesnost rozpoznávání.

Účelem DSR bylo standardizovat rozhraní mezi mobilním zařízením a rozpoznávacím serverem, čímž se zajistila interoperabilita. Řešilo to omezení rozpoznávání pouze na zařízení, které bylo limitováno omezeným výpočetním výkonem a pamětí UE, což znemožňovalo hostovat velké slovníky nebo komplexní modely. Rozdělením procesu DSR využilo výpočetní zdroje sítě k poskytnutí výkonnější a aktualizovatelné služby, zatímco standardizovaný front-end zajistil, že příznaky odesílané na server byly čisté a optimalizované pro rozpoznávání, nikoli pro poslech, čímž se zlepšila celková přesnost a spolehlivost napříč různými sítěmi a zařízeními.

## Klíčové vlastnosti

- Standardizovaná extrakce příznaků ve front-endu (ETSI ES 201 108/3GPP 26.243)
- Robustní přenos řečových příznaků přes kanály náchylné k chybám
- Oddělení akustického zpracování (klient) od lingvistického dekódování (server)
- Efektivita využití šířky pásma ve srovnání s přenosem plnopásmového zvuku
- Nezávislost na hlasovém telefonním kodeku a jeho artefaktech
- Podpora aktualizací akustických a jazykových modelů na straně serveru

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TS 26.177** (Rel-19) — DSR Extended Advanced Front-end Test Sequences
- **TS 26.235** (Rel-12) — Default Codecs for 3GPP IP Multimedia Subsystem
- **TS 26.236** (Rel-12) — Packet Switched Conversational Multimedia Protocols
- **TS 26.243** (Rel-19) — DSR Extended Advanced Front-end C Code
- **TR 26.943** (Rel-19) — SES Codec Selection Report
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.322** (Rel-19) — NR Radio Link Control (RLC) Protocol
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [DSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/dsr/)
