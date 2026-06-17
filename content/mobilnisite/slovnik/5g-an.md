---
slug: "5g-an"
url: "/mobilnisite/slovnik/5g-an/"
type: "slovnik"
title: "5G-AN – 5G Access Network"
date: 2026-01-01
abbr: "5G-AN"
fullName: "5G Access Network"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5g-an/"
summary: "Přístupová síť 5G (5G-AN) je souhrnné označení pro infrastrukturu rádiového přístupu spojující uživatelská zařízení s 5G Core sítí. Zahrnuje všechny technologie rádiového přístupu, včetně NG-RAN a ne-"
---

5G-AN je souhrnné označení pro infrastrukturu rádiového přístupu, včetně NG-RAN a integrovaných ne-3GPP technologií jako Wi-Fi, která připojuje uživatelská zařízení k 5G Core síti.

## Popis

Přístupová síť 5G (5G-AN) je základní architektonická komponenta definovaná v 5G systému (5GS) od 3GPP. Slouží jako zastřešující termín pro celou přístupovou vrstvu (access stratum), která poskytuje rádiové rozhraní a konektivitu mezi uživatelským zařízením (UE) a 5G Core sítí (5GC). Její primární funkcí je správa rádiových zdrojů a vytváření datových a signalizačních přenosových drah (bearers) potřebných pro komunikaci. Na rozdíl od předchozích generací, kde RAN byl synonymem pro konkrétní technologii (jako [E-UTRAN](/mobilnisite/slovnik/e-utran/) pro 4G), je 5G-AN definována abstraktněji a flexibilněji, aby podporovala multi-RAT (Radio Access Technology) prostředí.

Architektonicky je 5G-AN logicky oddělena od 5G Core přes standardizovaná rozhraní [N2](/mobilnisite/slovnik/n2/) (pro řídicí rovinu) a N3 (pro uživatelskou rovinu). Nejvýznamnější instancí 5G-AN je Next Generation Radio Access Network (NG-RAN), která se skládá z gNB (pro NR přístup) a ng-eNB (pro vyvinutý [E-UTRA](/mobilnisite/slovnik/e-utra/) přístup). Koncept 5G-AN je však širší a explicitně zahrnuje důvěryhodné a nedůvěryhodné ne-3GPP přístupové sítě, jako je Wi-Fi, které se mohou k 5GC připojit přes Non-3GPP InterWorking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)) nebo Trusted Non-3GPP Gateway Function (TNGF). Tento jednotný přístupový rámec je základním kamenem konvergenčních cílů 5G.

Z funkční perspektivy je 5G-AN zodpovědná za klíčové rádiové procedury. To zahrnuje správu rádiových zdrojů (RRM), řízení mobility spojení, plánování a přenos dat uživatelské a řídicí roviny přes rádiové rozhraní a vynucování QoS politik přijatých od 5GC přes rozhraní N2. Nespravuje sama sezení ani politiky; to jsou funkce core sítě. Místo toho jedná na základě rozhodnutí a parametrů (jako popisy QoS Flow a rozpočty zpoždění paketů) poskytnutých funkcí [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function) a [SMF](/mobilnisite/slovnik/smf/) (Session Management Function). Provoz 5G-AN je řízen protokolem [NG](/mobilnisite/slovnik/ng/) Application Protocol ([NGAP](/mobilnisite/slovnik/ngap/)) přes rozhraní N2 pro signalizaci řídicí roviny.

Role 5G-AN je klíčová pro dosažení hlavních výkonnostních ukazatelů 5G. Přímo ovlivňuje metriky uživatelského zážitku, jako je propustnost, latence a spolehlivost. Díky abstrakci konkrétní přístupové technologie může 5GC spravovat mobilitu a sezení bezproblémově napříč heterogenními typy přístupu (např. předání z NR na důvěryhodnou WLAN), což umožňuje skutečně přístupově agnostické služby. Dále podpora síťového řezání (network slicing) začíná v 5G-AN, protože ta musí být schopna identifikovat a aplikovat specifické konfigurace rádiových zdrojů pro různé síťové řezy na základě instrukcí z core sítě.

## K čemu slouží

Koncept 5G-AN byl vytvořen, aby řešil omezení předchozích celulárních architektur, které byly z velké části postaveny kolem jedné dominantní technologie rádiového přístupu. Ve 4G EPS byl E-UTRAN navržen speciálně pro LTE. To vytvářelo integrační výzvy pro jiné typy přístupu, které byly často považovány za sekundární nebo externí sítě. Hlavní motivací pro definici 5G-AN bylo architektonicky zakotvit princip agnosticismu přístupové sítě od samého počátku ve specifikaci 5G systému.

Tento přístup řeší několik klíčových problémů. Za prvé, budoucí vývoj 5GS je chráněn oddělením návrhu core sítě od specifik konkrétní rádiové technologie. Core síť komunikuje s 'přístupovou sítí' přes standardizovaná rozhraní (N2, N3), bez ohledu na to, zda tato přístupová síť používá 3GPP NR, vyvinuté LTE nebo Wi-Fi. To zjednodušuje integraci nových rádiových technologií, jak se objevují. Za druhé, umožňuje bezproblémovou kontinuitu služeb a jednotné vynucování politik napříč všemi typy přístupu, což je požadavek pro poskytování konzistentního uživatelského zážitku ve světě, kde zařízení často přepínají mezi celulární sítí a Wi-Fi. Nakonec poskytuje čistý rámec pro síťové řezání, umožňující, aby konfigurace a výkonnostní cíle specifické pro řez byly komunikovány a vynucovány podkladovou rádiovou vrstvou, bez ohledu na použitou RAT.

## Klíčové vlastnosti

- Jednotná abstrakce pro více technologií rádiového přístupu (3GPP i ne-3GPP)
- Standardizovaná rozhraní řídicí roviny (N2) a uživatelské roviny (N3) k 5G Core
- Podpora integrovaného přístupu včetně NG-RAN (gNB/ng-eNB) a důvěryhodného/nedůvěryhodného ne-3GPP přístupu
- Vynucování QoS politik a rozpočtů zpoždění paketů odvozených od core sítě na rádiové vrstvě
- Základ pro přístupově agnostické řízení mobility a kontinuitu sezení
- Nezbytná komponenta pro realizaci end-to-end síťového řezání napříč RAN

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 32.256** (Rel-19) — 5G Connection & Mobility Charging Spec
- **TS 32.404** (Rel-19) — Performance Management Definitions & Template
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.861** (Rel-16) — CIoT Security Evolution for 5G System

---

📖 **Anglický originál a plná specifikace:** [5G-AN na 3GPP Explorer](https://3gpp-explorer.com/glossary/5g-an/)
