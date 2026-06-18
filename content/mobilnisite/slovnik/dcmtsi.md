---
slug: "dcmtsi"
url: "/mobilnisite/slovnik/dcmtsi/"
type: "slovnik"
title: "DCMTSI – Data Channel Multimedia Telephony Service over IMS"
date: 2026-01-01
abbr: "DCMTSI"
fullName: "Data Channel Multimedia Telephony Service over IMS"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dcmtsi/"
summary: "DCMTSI je služba standardizovaná 3GPP, která umožňuje multimediální telefonii v reálném čase přes IMS s využitím datových kanálů WebRTC. Podporuje hlas, video a sdílení dat v rámci jediné relace, čímž"
---

DCMTSI je služba standardizovaná 3GPP, která umožňuje multimediální telefonii v reálném čase přes IMS s využitím datových kanálů WebRTC pro podporu hlasu, videa a sdílení dat v rámci jediné relace.

## Popis

Data Channel Multimedia Telephony Service over IMS (DCMTSI) je architektura služby 3GPP, která využívá IP Multimedia Subsystem (IMS) k poskytování služeb multimediální telefonie s použitím datových kanálů WebRTC (Web Real-Time Communication) jako transportního mechanismu. Funguje tak, že mezi koncovými body, jako jsou webové prohlížeče nebo nativní aplikace, naváže multimediální relaci prostřednictvím signalizace IMS (primárně [SIP](/mobilnisite/slovnik/sip/) a [SDP](/mobilnisite/slovnik/sdp/)) a následně využije datové kanály WebRTC k přenosu mediálních proudů v reálném čase (hlas, video) a libovolných dat (např. přenos souborů, textový chat) v rámci této relace. Služba je definována tak, aby zajistila interoperabilitu mezi klienty založenými na WebRTC a tradičními telefonními sítěmi založenými na IMS, což umožňuje bohaté konverzační multimediální zážitky.

Architektonicky DCMTSI integruje jádro IMS (včetně CSCFs, [HSS](/mobilnisite/slovnik/hss/)) s koncovými body podporujícími WebRTC. IMS poskytuje autentizaci, autorizaci, řízení relací a orchestraci služeb. Framework WebRTC, konkrétně jeho [API](/mobilnisite/slovnik/api/) pro datové kanály postavené na [SCTP](/mobilnisite/slovnik/sctp/) přes [DTLS](/mobilnisite/slovnik/dtls/), poskytuje zabezpečený obousměrný transport pro média a data. Mezi klíčové komponenty patří klient DCMTSI (WebRTC aplikace implementující profily 3GPP), prvky jádrové sítě IMS a často WebRTC brána nebo aplikační server IMS ([AS](/mobilnisite/slovnik/as/)), který může adaptovat protokoly mezi světem WebRTC a sítí IMS. Služba používá standardní postupy IMS pro registraci a navázání relace, s rozšířeními SDP pro vyjednání použití datových kanálů pro média.

Při provozu začíná relace DCMTSI registrací a autentizací klienta v IMS. Pro zahájení hovoru klient odešle SIP INVITE obsahující SDP nabídku, která indikuje podporu médií přes datové kanály WebRTC. Po přijetí jádro IMS směruje signalizaci a usnadňuje nastavení relace. Koncové body následně navážou přímé nebo přes relay přepojované peer-to-peer spojení datového kanálu WebRTC pro tok médií, s využitím [ICE](/mobilnisite/slovnik/ice/) pro průchod NAT, DTLS pro zabezpečení a SCTP pro transport. To umožňuje synchronní přenos více typů médií v rámci stejného logického kanálu. Služba podporuje základní telefonní funkce jako podržení hovoru, přepojení a konference, řízené signalizací IMS, zatímco média proudí přes datové kanály.

Úlohou DCMTSI v síti je rozšířit telefonní služby založené na IMS na klienty WebRTC bez nutnosti plnohodnotného tradičního uživatelského zařízení (UE) IMS. Umožňuje poskytovatelům služeb nabízet multimediální komunikaci na úrovni operátora (hlas, video, data) uživatelům ve webových prohlížečích nebo lehkých aplikacích, přičemž využívá stávající infrastrukturu IMS pro řízení a účtování. Tím překlenuje propast mezi telekomunikačními sítěmi a komunikací založenou na internetu a usnadňuje konvergenci služeb.

## K čemu slouží

DCMTSI bylo vytvořeno, aby řešilo rostoucí poptávku po integraci webových komunikačních technologií, konkrétně WebRTC, se standardizovanými telekomunikačními sítěmi jako je IMS. Historicky byly služby IMS primárně přístupné přes dedikovaná uživatelská zařízení (UE) se složitými zásobníky, zatímco WebRTC nabízelo komunikaci v reálném čase založenou na prohlížeči, ale postrádalo standardizovanou integraci do sítí operátorů. To vytvořilo propast: webové aplikace nemohly snadno přistupovat k bohatým telefonním službám (např. garantovaná QoS, tísňové volání, interoperabilita mezi operátory) poskytovaným IMS. DCMTSI to řeší definováním standardizované metody použití datových kanálů WebRTC jako mediálního transportu pro multimediální telefonii IMS, což umožňuje webovým klientům stát se plnohodnotnými účastníky v sítích IMS.

Motivace vychází z potřeby poskytovatelů služeb nabízet konzistentní, funkčně bohaté komunikační zážitky na všech zařízeních, včetně webových prohlížečů a mobilních aplikací, bez nutnosti vyvíjet proprietární řešení. Před DCMTSI byla integrace WebRTC s IMS možná, ale nebyla standardizovaná, což vedlo k fragmentaci a problémům s interoperabilitou. DCMTSI poskytuje přístup specifikovaný 3GPP, který zajišťuje, že služby jako vysoce kvalitní hlasové/videohovory, okamžité zasílání zpráv a sdílení souborů mohou být bezproblémově doručovány přes IMS na koncové body WebRTC. Využívá silné stránky obou: IMS pro řízení jádrové sítě, zabezpečení a integraci služeb a WebRTC pro snadné nasazení klienta a pokročilé mediální schopnosti.

Dále DCMTSI řeší omezení dřívějších přístupů jako Voice over LTE (VoLTE) a Video over LTE (ViLTE), které vyžadovaly specifické implementace uživatelského zařízení (UE). Použitím datových kanálů WebRTC umožňuje DCMTSI flexibilnější zacházení s médii (např. kombinaci sdílení dat s hlasem/videem) a zjednodušuje vývoj klienta. Podporuje vývoj směrem k plně IP sítím a konvergenci telekomunikačních a webových služeb, což operátorům umožňuje rychle nasazovat inovativní multimediální služby a rozšiřovat své investice do IMS na širší škálu zařízení a aplikací.

## Klíčové vlastnosti

- Standardizovaná integrace datových kanálů WebRTC s IMS pro mediální transport
- Podpora současného sdílení hlasu, videa a libovolných dat v rámci jediné relace
- Využívá IMS pro autentizaci, řízení relací a orchestraci služeb
- Využívá protokoly WebRTC (SCTP/DTLS) pro zabezpečené a spolehlivé doručování médií
- Umožňuje webovým prohlížečům a aplikacím fungovat jako klienti multimediální telefonie IMS
- Podporuje základní telefonní funkce jako podržení hovoru, přepojení a konference prostřednictvím signalizace IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.392** (Rel-19) — MMTel Application Enablement
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.567** (Rel-19) — IMS-based Split Rendering
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TR 33.890** (Rel-18) — Technical Report on Security Aspects

---

📖 **Anglický originál a plná specifikace:** [DCMTSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcmtsi/)
