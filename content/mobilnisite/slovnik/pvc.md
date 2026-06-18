---
slug: "pvc"
url: "/mobilnisite/slovnik/pvc/"
type: "slovnik"
title: "PVC – Permanent Virtual Circuit"
date: 2025-01-01
abbr: "PVC"
fullName: "Permanent Virtual Circuit"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pvc/"
summary: "Permanent Virtual Circuit (PVC) je předem nakonfigurovaná, trvalá logická komunikační cesta zřízená v paketové síti, například na bázi Frame Relay nebo ATM. Poskytuje stálé spojení mezi dvěma síťovými"
---

PVC je předem nakonfigurovaná trvalá logická cesta v paketové síti, která poskytuje stálé spojení mezi koncovými body (např. SGSN a GGSN) a imituje vyhrazenou linku přes sdílenou infrastrukturu.

## Popis

Permanent Virtual Circuit (PVC) je klíčový síťový koncept z období spojově orientovaných paketových technologií, jako jsou Frame Relay a Asynchronous Transfer Mode ([ATM](/mobilnisite/slovnik/atm/)), které byly široce používány v raných páteřních sítích 3GPP jádra (např. [GPRS](/mobilnisite/slovnik/gprs/), UMTS). Na rozdíl od Switched Virtual Circuit ([SVC](/mobilnisite/slovnik/svc/)), který se zřizuje dynamicky na požádání, je PVC staticky zřízeno operátorem sítě. Definuje trvalou logickou trasu, identifikovanou Data Link Connection Identifier ([DLCI](/mobilnisite/slovnik/dlci/)) ve Frame Relay nebo dvojicí Virtual Path Identifier/Virtual Channel Identifier (VPI/VCI) v ATM, mezi dvěma koncovými body v síti. Tato trasa je 'virtuální', protože nepředstavuje vyhrazený fyzický kabel; místo toho jde o předdefinovanou cestu přes síť přepínačů, kde statistické multiplexování umožňuje sdílené fyzické infrastruktuře přenášet provoz pro mnoho takových PVC současně.

Z architektonického hlediska se PVC zřizuje manuální konfigurací na zúčastněných síťových přepínačích (Frame Relay nebo ATM přepínačích). Operátor definuje koncové body (např. port a DLCI na přepínači A směrem k portu a DLCI na přepínači Z) a přenosové parametry okruhu, jako je Committed Information Rate ([CIR](/mobilnisite/slovnik/cir/)) a Burst Information Rate ([BIR](/mobilnisite/slovnik/bir/)). Tyto parametry definují garantovanou a maximální šířku pásma pro PVC. Po nakonfigurování je cesta trvale k dispozici v routovacích tabulkách přepínačů a připravena přeposílat buňky nebo rámce. V kontextu 3GPP se PVC běžně používaly k vytvoření spolehlivých přenosových spojů mezi uzly jádrové sítě. Například v síti GPRS se PVC zřizovala přes páteř ATM nebo Frame Relay pro propojení Serving GPRS Support Nodes ([SGSN](/mobilnisite/slovnik/sgsn/)) s Gateway GPRS Support Nodes (GGSN) a tvořila tak přenosovou páteř pro tunely GPRS Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)).

Provoz PVC je z pohledu koncových bodů relativně jednoduchý. Síťová karta nakonfigurovaná s konkrétním PVC (pomocí jeho DLCI nebo VPI/VCI) s ním zachází jako s trvalou odchozí cestou. Jakákoli data odeslaná na toto logické rozhraní jsou zapouzdřena do příslušného rámce Frame Relay nebo buňky ATM a vložena do sítě. Předem nakonfigurované přepínače podél cesty prozkoumají identifikátor spojení v hlavičce a přeposílají provoz na další hop podle statického mapování, až jej doručí cílovému koncovému bodu. To poskytuje předvídatelnou latenci a známou cestu, což je výhodné pro plánování sítě a řešení problémů. PVC však postrádají flexibilitu spojení zřizovaných na požádání a mohou vést k neefektivnímu využití zdrojů, pokud není předdefinovaná šířka pásma plně využita.

## K čemu slouží

Technologie PVC byla vytvořena, aby poskytla cenově efektivní, spolehlivou a předvídatelnou konektivitu pro podnikové a přenosové sítě před masovým rozšířením IP/Ethernetu jako univerzálního řešení na vrstvě 2 a 3. Řešila potřebu více trvalých point-to-point spojů (jako jsou pronajaté linky) bez neúměrných nákladů na budování samostatných fyzických okruhů pro každé spojení. Použitím PVC přes sdílenou 'cloudovou' infrastrukturu Frame Relay nebo ATM mohly organizace propojit více lokalit s jediným fyzickým přístupovým spojem k poskytovateli služeb, což dramaticky snížilo náklady při zachování vzhledu a předvídatelnosti vyhrazených okruhů.

V historickém kontextu sítí 3GPP (2G GPRS a 3G UMTS) ještě nebyla IP infrastruktura v přenosových páteřích všudypřítomná nebo dostatečně robustní. Frame Relay a ATM nabízely funkce na úrovni přenosové sítě se silným řízením provozu, garancemi kvality služby (QoS) prostřednictvím parametrů jako CIR a spolehlivým provozem. PVC vyřešily problém propojení nově definovaných paketových uzlů jádra (SGSN, GGSN) stabilním a řiditelným způsobem. Poskytovaly předvídatelný přenos nezbytný pro GTP tunely přenášející uživatelská data. Omezení, které PVC řešily, byla neefektivita a vysoká cena fyzických síťových meshů, ale samy zavedly omezení statické konfigurace, které bylo později překonáno dynamickou, nespojovou povahou IP routingu ve vyvinutých jádrech 3GPP, jako je Evolved Packet Core (EPC) a 5G Core (5GC), kde Ethernet a IP transport nahradily ATM/Frame Relay a PVC.

## Klíčové vlastnosti

- Staticky zřízené a trvalé logické spojení, nevyžadující navolování/ukončování spojení pro každou relaci (call setup/teardown)
- Identifikováno logickým identifikátorem (DLCI pro Frame Relay, VPI/VCI pro ATM)
- Poskytuje předvídatelnou cestu a výkonnostní charakteristiky (např. garantovanou CIR)
- Umožňuje statistické multiplexování více logických okruhů přes sdílené fyzické linky
- Podporuje kvalitu služeb prostřednictvím parametrů přenosové smlouvy
- Používáno jako stabilní transport pro protokoly vyšších vrstev, jako je GTP, v legacy jádrech GPRS/UMTS

## Související pojmy

- [SVC – Switched Virtual Circuit](/mobilnisite/slovnik/svc/)
- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 24.819** (Rel-7) — IMS Services via Fixed Broadband Access
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols
- **TS 32.407** (Rel-19) — PM; CN CS Domain; UMTS/GSM measurements
- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [PVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/pvc/)
