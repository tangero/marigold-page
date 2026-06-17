---
slug: "mlp"
url: "/mobilnisite/slovnik/mlp/"
type: "slovnik"
title: "MLP – Mobile Location Protocol"
date: 2025-01-01
abbr: "MLP"
fullName: "Mobile Location Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mlp/"
summary: "Aplikační protokol standardizovaný Open Mobile Alliance (OMA) a odkazovaný 3GPP pro výměnu lokalizačních informací mezi lokalizačním serverem (např. GMLC) a klientem lokalizační služby (LCS Client). U"
---

MLP je aplikační protokol standardizovaný organizací OMA a odkazovaný 3GPP pro výměnu lokalizačních informací mezi lokalizačním serverem a klientem za účelem zpřístupnění určování polohy mobilního zařízení.

## Popis

Mobile Location Protocol (MLP) je XML aplikační protokol používaný pro vyžádání a doručení informace o poloze mobilní stanice ([MS](/mobilnisite/slovnik/ms/)). Funguje mezi klientem lokalizační služby ([LCS](/mobilnisite/slovnik/lcs/) Client) a lokalizačním serverem, jako je Gateway Mobile Location Center ([GMLC](/mobilnisite/slovnik/gmlc/)) v síti 3GPP. MLP poskytuje standardizované rozhraní, které abstrahuje od podkladových síťově specifických lokalizačních technologií (např. Cell-ID, [OTDOA](/mobilnisite/slovnik/otdoa/), [A-GPS](/mobilnisite/slovnik/a-gps/)), což umožňuje službám a aplikacím vyžádat si polohu jednotným způsobem. Protokol definuje sadu služebních primitiv pro různé typy lokalizačních požadavků, včetně okamžitého určení polohy, spouštěného hlášení polohy a standardního hlášení polohy.

Jádrem MLP je jeho model požadavek-odpověď využívající XML dokumenty přenášené přes [HTTP](/mobilnisite/slovnik/http/)/[HTTPS](/mobilnisite/slovnik/https/) nebo jiný transport. Typická výměna MLP zahrnuje odeslání standardizovaného MLP služebního požadavku (např. Standard Location Immediate Request - SLIR) od klienta LCS na lokalizační server. Tento požadavek obsahuje parametry jako cílové [MSISDN](/mobilnisite/slovnik/msisdn/) nebo IMSI, požadovanou kvalitu služby (QoS), například přesnost a dobu odezvy, a typ odhadu polohy (např. zeměpisná šířka/délka). Lokalizační server požadavek ověří a autorizuje, komunikuje s lokalizačními subsystémy mobilní sítě (jako je Serving Mobile Location Center - SMLC) za účelem získání polohy a následně sestaví MLP služební odpověď (např. Standard Location Immediate Answer - SLIA) zpět klientovi, která obsahuje odhad polohy nebo kód chyby.

MLP podporuje více typů služeb pro různé potřeby aplikací. Služba Immediate Service slouží pro jednorázové získání polohy. Služba Triggered Service umožňuje klientovi nastavit odběr pro periodické nebo událostmi řízené hlášení polohy (např. když zařízení vstoupí do definované oblasti). Služba Reporting Service je používána sítí pro zaslání lokalizační informace klientovi, obvykle následně po spouštěcí události. MLP také definuje prvky pro ochranu soukromí a zabezpečení, zajišťující, aby lokalizační požadavky odpovídaly uživatelským nastavením soukromí a aby komunikace mezi klientem a serverem byla bezpečná. V rámci 3GPP je MLP specifikován jako klíčové externí rozhraní (rozhraní Le) pro Gateway Mobile Location Center (GMLC), umožňující zákonné odposlechy, nouzové služby (E911/E112) a komerční lokalizační služby (LBS) jako navigaci, vyhledávač přátel nebo sledování majetku.

## K čemu slouží

MLP byl vyvinut k řešení problému proprietárních a fragmentovaných rozhraní pro přístup k poloze mobilního zařízení. V počátcích lokalizačních služeb používali výrobci síťových zařízení a poskytovatelé služeb často vlastní protokoly, což bránilo interoperabilitě a zpomalovalo vývoj širokého ekosystému LBS aplikací. Vytvoření standardizovaného aplikačního protokolu bylo motivováno potřebou poskytnout jednotný a konzistentní způsob, jakým autorizované externí aplikace mohou žádat o lokalizační informace, bez ohledu na podkladovou síťovou technologii (GSM, UMTS, LTE) nebo použitou metodu určování polohy.

Jeho přijetí organizací 3GPP a standardizace Open Mobile Alliance (OMA) poskytla potřebný společný jazyk mezi poskytovateli služeb a mobilními operátory. To umožnilo škálovatelné nasazení komerčních LBS, nouzových služeb (kde jsou standardizovaná rozhraní klíčová pro připojení PSAP) a přidružených služeb. MLP abstrahuje složitosti rádiové přístupové sítě, což umožňuje vývojářům aplikací soustředit se na služební logiku namísto síťové integrace, a tím podporuje inovace na trhu lokalizačních služeb.

## Klíčové vlastnosti

- Protokol založený na XML pro strukturované lokalizační zprávy požadavků a odpovědí
- Podpora typů lokalizačních služeb: okamžitá, spouštěná a hlášení polohy
- Definice standardizovaných parametrů QoS pro přesnost polohy a dobu odezvy
- Transport přes HTTP/HTTPS pro snadnou integraci s webovými technologiemi
- Vestavěné mechanismy pro zpracování ochrany soukromí a autorizace
- Standardizované kódy chyb a hlášení pro robustní provoz služby

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 26.851** (Rel-11) — Enhancements to Multimedia (EMM) for PSS, MMS, MBMS
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services

---

📖 **Anglický originál a plná specifikace:** [MLP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mlp/)
