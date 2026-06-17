---
slug: "isup"
url: "/mobilnisite/slovnik/isup/"
type: "slovnik"
title: "ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension"
date: 2025-01-01
abbr: "ISUP"
fullName: "MIME ISDN User Part Multi-purpose Internet Mail Extension"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/isup/"
summary: "ISUP v kontextu MIME rozšíření označuje adaptaci tradičního signalizačního protokolu ISDN User Part pro přenos přes IP sítě s využitím MIME enkapsulace. Umožňuje přenos zastaralé signalizace řízení ho"
---

ISUP je adaptace tradiční signalizačního protokolu ISDN User Part pro přenos přes IP sítě s využitím MIME enkapsulace, což umožňuje provoz zastaralé signalizace řízení hovorů v rámci SIP architektur pro propojování sítí.

## Popis

[MIME](/mobilnisite/slovnik/mime/) [ISDN](/mobilnisite/slovnik/isdn/) User Part (ISUP) je specifikace pro enkapsulaci a přenos zpráv z protokolu ISDN User Part – klíčové součásti signalizačního systému č. 7 (SS7) používaného pro navazování, správu a ukončování telefonních hovorů ve veřejné telefonní síti (PSTN) – v rámci protokolů založených na IP. Využívá formát Multi-purpose Internet Mail Extensions (MIME) k zabalení binárního obsahu ISUP zprávy do formátu vhodného pro přenos přes sítě TCP/IP, typicky v těle zprávy Session Initiation Protocol (SIP) nebo jiné IP signalizační přenosové jednotky. Tato enkapsulace umožňuje Media Gateway Controlleru ([MGC](/mobilnisite/slovnik/mgc/)) nebo softswitchu interpretovat a generovat ISUP signalizaci bez přímého propojení založeného na TDM a SS7, což umožňuje bezproblémové řízení hovorů mezi IP sítěmi (jako je IMS) a zastaralou PSTN nebo PLMN. Proces zahrnuje signalizační bránu, která provádí konverzi protokolů a mapuje parametry ISUP do enkapsulovaného MIME formátu a zpět. Mezi klíčové architektonické komponenty patří signalizační brána (SG) pro propojení SS7/IP, Media Gateway Controller pro logiku řízení hovorů a aplikační servery, které zpracovávají obsah kódovaný v MIME. Jeho role je klíčová při přechodu na plně IP sítě, neboť poskytuje standardizovanou metodu pro zachování bohaté signalizační informace spojené s hovorem, jako je identifikace volajícího, indikace přesměrování hovoru a příčinné kódy, během průchodu sítí.

## K čemu slouží

[MIME](/mobilnisite/slovnik/mime/) enkapsulace pro ISUP byla vyvinuta k řešení problému propojení vznikajících telefonních sítí založených na IP (jako jsou ty založené na SIP) a zavedené globální infrastruktury PSTN/PLMN, která spoléhá na signalizaci SS7 a ISUP. Když operátoři začali nasazovat sítě Voice over IP (VoIP) a IMS, byla potřeba metoda pro transparentní přenos sofistikovaných informací řízení hovorů přítomných v ISUP zprávách přes IP hranice bez ztráty funkčnosti. Předchozí přístupy zahrnovaly jednodušší mapování parametrů, které mohlo vést ke ztrátě informací nebo vyžadovalo proprietární rozšíření. Použití MIME poskytuje flexibilní, standardizovaný kontejner definovaný v [IETF](/mobilnisite/slovnik/ietf/) a 3GPP, který může nést kompletní, nezměněný obsah ISUP zprávy, čímž zajišťuje plnou transparentnost funkcí a podporuje pokročilé telefonní služby během migrační fáze. Jeho vznik byl motivován pohybem průmyslu směrem ke konvergenci sítí a potřebou budoucně odolného, rozšiřitelného mechanismu pro zvládnutí signalizačního propojení v sítích nové generace ([NGN](/mobilnisite/slovnik/ngn/)).

## Klíčové vlastnosti

- Enkapsulace binárních ISUP zpráv v rámci částí těla MIME
- Přenos v rámci SIP zpráv (např. v SIP INVITE nebo INFO požadavcích)
- Podpora transparentnosti všech parametrů a příčinných kódů ISUP
- Umožňuje propojení mezi IP řízením hovorů a zastaralými SS7 sítěmi
- Definován pro použití v 3GPP IMS a dalších architekturách NGN
- Usnadňuje implementaci trunkingových bran a softswitchů

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.508** (Rel-8) — TIP and TIR Service Protocol Description
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways
- **TS 29.458** (Rel-8) — SIP Transfer of Tariff Info for Charging
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [ISUP na 3GPP Explorer](https://3gpp-explorer.com/glossary/isup/)
