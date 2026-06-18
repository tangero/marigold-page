---
slug: "pfd"
url: "/mobilnisite/slovnik/pfd/"
type: "slovnik"
title: "PFD – Packet Flow Description"
date: 2026-01-01
abbr: "PFD"
fullName: "Packet Flow Description"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pfd/"
summary: "Soubor informací používaný k identifikaci aplikačního provozu za účelem aplikace specifických politik. Obsahuje identifikátory aplikací a s nimi asociované paketové filtry (např. URL, doménová jména,"
---

PFD je soubor informací obsahující identifikátory aplikací a paketové filtry, který slouží k identifikaci aplikačního provozu za účelem aplikace specifických politik.

## Popis

Packet Flow Description (PFD) je datový objekt používaný v rámci rámce pro řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) 3GPP k umožnění správy sítě s ohledem na aplikace. Jeho hlavním účelem je poskytnout User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) nebo Traffic Detection Function ([TDF](/mobilnisite/slovnik/tdf/)) nezbytné informace pro detekci provozu náležejícího konkrétní aplikaci, jako je služba streamování videa nebo aplikace sociálních médií. PFD není pravidlo samo o sobě, ale popisný vstup použitý k vytvoření Packet Detection Rules (PDRs) v rámci protokolu [PFCP](/mobilnisite/slovnik/pfcp/). PFD typicky obsahuje identifikátor aplikace (např. standardizované 3GPP App ID nebo vlastní identifikátor) a jeden či více paketových filtrů.

Tyto paketové filtry mohou být definovány na různých vrstvách síťového modelu, což umožňuje flexibilní a efektivní detekci. Mohou zahrnovat doménová jména, [URL](/mobilnisite/slovnik/url/), vzory [URI](/mobilnisite/slovnik/uri/) nebo tradiční 3-tice/5-tice IP informací (zdrojová/cílová IP adresa, protokol, čísla portů). Například PFD pro videoslužbu může obsahovat doménové jméno její sítě pro doručování obsahu a specifické vzory URL pro video segmenty. Subjekt odpovědný za správu PFD, jako je Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) nebo Application Function ([AF](/mobilnisite/slovnik/af/)), zřizuje tyto PFD pro SMF přes rozhraní N5/N7. SMF následně překládá PFD do akčních Packet Detection Rules (PDRs) a instaluje je do příslušné UPF pomocí protokolu PFCP.

Po instalaci UPF používá tato odvozená pravidla k inspekci paketů. Když dojde k shodě, může UPF aplikovat příslušnou politiku, jako je směrování provozu na konkrétní edge server, aplikace priorit QoS, spuštění účtovacích událostí nebo blokování toku. Tento mechanismus je klíčový pro diferenciaci služeb, optimalizaci sítě a rodičovské kontroly. Rámec PFD také zahrnuje procedury pro správu PFD, což umožňuje PCF dynamicky zřizovat, aktualizovat nebo odebírat PFD, a tím umožňuje přizpůsobení schopností detekce aplikací v síti v reálném čase, jak se objevují nové služby nebo mění vzorce provozu.

## K čemu slouží

Packet Flow Description byl vyvinut k řešení výzvy efektivní identifikace a správy explodujícího množství různorodého provozu Over-The-Top (OTT) aplikací v mobilních sítích. Tradiční řízení politik se silně opíralo o statická, operátorem definovaná pravidla založená na IP adresách a číslech portů, která se stala neúčinnými, protože aplikace začaly používat dynamické porty, šifrované protokoly (jako HTTPS) a sdílené sítě pro doručování obsahu, což zastřelo jejich identitu.

PFD poskytují standardizovanou, flexibilní metodu pro popis aplikačního provozu nad rámec omezené 5-tice. Začleněním identifikátorů aplikační vrstvy, jako jsou doménová jména a vzory URL, umožňují mnohem přesnější detekci provozu. Tato přesnost je zásadní pro implementaci pokročilých politik, jako je sponzorované datování (kde poskytovatel aplikace platí za datové využití), aplikace-specifické zvýšení QoS (např. zvýšení priority partnerské videoslužby) a inteligentní směrování provozu k lokálním breakouts nebo edge cache. Rámec PFD, zavedený jako součást vylepšeného řízení politik, umožňuje operátorům a poskytovatelům služeb třetích stran spolupracovat na vytváření sítí s ohledem na aplikace, což znamená přechod od správy anonymních IP přenosů ke správě rozpoznaných služeb a uživatelských zkušeností.

## Klíčové vlastnosti

- Obsahuje identifikátory aplikací a paketové filtry pro přesnou detekci provozu
- Podporuje vícevrstvé filtry včetně doménových jmen, URL a IP n-tic
- Zřizováno PCF/AF pro SMF přes služební rozhraní (např. N5, N7)
- Překládáno SMF do PFCP Packet Detection Rules (PDRs) pro vynucení v UPF
- Umožňuje dynamickou správu (zřizování, aktualizaci, odstranění) detekčních kritérií
- Základní prvek pro politiky, účtování a směrování provozu s ohledem na aplikace

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.250** (Rel-19) — Nu Reference Point Stage 3 Specification
- **TS 29.251** (Rel-19) — Gw/Gwn Reference Points Stage 3 Specification
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.519** (Rel-19) — UDR Usage for Policy & Exposure Data
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [PFD na 3GPP Explorer](https://3gpp-explorer.com/glossary/pfd/)
