---
slug: "mpquic"
url: "/mobilnisite/slovnik/mpquic/"
type: "slovnik"
title: "MPQUIC – Multi-Path QUIC"
date: 2026-01-01
abbr: "MPQUIC"
fullName: "Multi-Path QUIC"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mpquic/"
summary: "MPQUIC je rozšíření transportního protokolu umožňující simultánní přenos dat po více síťových cestách, například 5G a Wi-Fi. Zvyšuje propustnost, snižuje latenci a zlepšuje odolnost spojení agregací š"
---

MPQUIC je rozšíření transportního protokolu, které umožňuje simultánní přenos dat po více síťových cestách za účelem zvýšení propustnosti, snížení latence a zlepšení odolnosti spojení.

## Popis

Multi-Path [QUIC](/mobilnisite/slovnik/quic/) (MPQUIC) je rozšíření transportního protokolu QUIC, standardizované organizací [IETF](/mobilnisite/slovnik/ietf/) a přijaté konsorciem 3GPP. Umožňuje, aby jediné QUIC spojení souběžně využívalo více různých síťových cest. Toho je dosaženo vytvořením více podtoků v rámci jednoho spojení, z nichž každý je vázán na jinou 5-tici (zdrojová IP adresa, zdrojový port, cílová IP adresa, cílový port, transportní protokol). Každý podtok funguje nezávisle se svým vlastním řízením zahlcení a číslováním paketů, ale sdílejí společný kryptografický a spojovací kontext. Protokol inteligentně plánuje odesílání paketů přes dostupné cesty na základě jejich charakteristik v reálném čase, jako je latence, ztrátovost a dostupná šířka pásma. Klíčovou architektonickou součástí je správce cest (path manager), který objevuje, ověřuje a monitoruje použitelnost každé potenciální cesty. MPQUIC také plynule zvládá migraci mezi cestami; pokud jedna cesta selže, provoz je okamžitě přesměrován na jiné aktivní cesty bez přerušení spojení na aplikační vrstvě. Tato vícecestná schopnost je integrována do architektury systému 5G, kde může využívat více [PDU](/mobilnisite/slovnik/pdu/) relací, více přístupových technologií (např. 3GPP a non-3GPP přístup) nebo různých funkcí uživatelské roviny. Jádrová síť 5G prostřednictvím entit jako [SMF](/mobilnisite/slovnik/smf/) a [UPF](/mobilnisite/slovnik/upf/) podporuje vytváření a řízení politik pro spojení, která mohou využívat MPQUIC. Z pohledu koncového bodu mohou zařízení s více rádiovými rozhraními (např. 5G NR a Wi-Fi) použít MPQUIC ke spojení těchto spojů, čímž se aplikační vrstvě prezentuje jediný, robustní a vysoce výkonný kanál.

## K čemu slouží

MPQUIC byl vytvořen, aby řešil omezení jednocestných transportních protokolů v stále více heterogenním a vícepřipojeném síťovém prostředí. Tradiční TCP a dokonce i jednocestný [QUIC](/mobilnisite/slovnik/quic/) jsou vázány na jednu síťovou cestu na spojení, což je činí náchylnými k výkonnostním úzkým místům nebo výpadkům této jediné cesty. S rozšířením zařízení vybavených více rádiovými rozhraními (např. 5G, LTE, Wi-Fi) se naskytla jasná příležitost ke zlepšení výkonu, spolehlivosti a uživatelského zážitku souběžným využíváním všech dostupných spojů. Primární problémy, které MPQUIC řeší, jsou: 1) Neefektivní využití prostředků, kdy je v daný čas používáno pouze jedno síťové rozhraní, přestože jiná jsou dostupná; 2) Špičky latence a přerušení spojení během předávání služeb nebo výpadků cest; a 3) Neschopnost agregovat šířku pásma z různorodých spojů pro splnění vysokých požadavků na propustnost moderních aplikací, jako je ultra-HD video, cloudové hraní her a přenosy rozsáhlých souborů. Historicky existovala řešení jako [MPTCP](/mobilnisite/slovnik/mptcp/), ale narážela na problémy s nasazením kvůli zásahům mezilehlých zařízení (middlebox) a složité síťové integraci. QUIC, jakožto protokol založený na [UDP](/mobilnisite/slovnik/udp/) a standardně šifrovaný, je vůči zásahům mezilehlých zařízení odolnější. Jeho rozšíření o vícecestné schopnosti (MPQUIC) poskytlo čistší a snáze nasaditelné řešení, které je v souladu s nativní podporou souběžného přístupu a síťového řezání (network slicing) v architektuře 5G. Jeho přijetí v 3GPP Rel-18 bylo motivováno potřebou zvýšené flexibility transportu pro podporu nových požadavků služeb, jako je imerzivní média, průmyslový IoT a spolehlivá vozidlová komunikace.

## Klíčové vlastnosti

- Souběžný vícecestný přenos přes heterogenní přístupy (např. 5G a Wi-Fi)
- Plynulá migrace mezi cestami a převzetí služeb při selhání bez přerušení aplikačního spojení
- Řízení zahlcení pro každou cestu zvlášť pro efektivní využití šířky pásma
- Agregovaná propustnost a snížená latence díky inteligentnímu plánování odesílání paketů
- Zvýšená odolnost a robustnost spojení vůči výpadkům jedné cesty
- Těsná integrace s architekturou systému 5G a správou PDU relací

## Související pojmy

- [QUIC – Quick UDP Internet Connections](/mobilnisite/slovnik/quic/)
- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [MPQUIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpquic/)
