---
slug: "ird"
url: "/mobilnisite/slovnik/ird/"
type: "slovnik"
title: "IRD – Integrated Receiver-Decoder"
date: 2025-01-01
abbr: "IRD"
fullName: "Integrated Receiver-Decoder"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ird/"
summary: "Funkční komponenta v architektuře 3GPP Media Streaming, která přijímá, dešifruje a dekóduje chráněné mediální streamy. Je klíčovou klientskou entitou v ekosystému 3GPP Dynamic Adaptive Streaming over"
---

IRD je klientská funkční komponenta v rámci 3GPP streamování médií, která přijímá, dešifruje a dekóduje chráněné mediální streamy pro zabezpečené dynamické adaptivní streamování přes HTTP (DASH).

## Popis

Integrated Receiver-Decoder (IRD) je logická funkční entita definovaná v architektuře 3GPP Media Streaming (M4S), konkrétně pro doručování chráněného mediálního obsahu. Nachází se v rámci klientské aplikace nebo zařízení (např. smartphone, tablet, TV). Primární role IRD je fungovat jako koncový bod pro zabezpečenou relaci doručování médií, která zahrnuje přijímání šifrovaných mediálních segmentů, jejich dešifrování a následné dekódování pro prezentaci. Z architektonického hlediska se nachází mezi streamovací logikou [DASH](/mobilnisite/slovnik/dash/) klienta a řetězcem pro přehrávání médií v zařízení. Přijímá Media Presentation Descriptions ([MPD](/mobilnisite/slovnik/mpd/)) a šifrované mediální segmenty prostřednictvím [HTTP](/mobilnisite/slovnik/http/) nebo [HTTPS](/mobilnisite/slovnik/https/), což typicky zajišťuje DASH klient.

IRD spolupracuje s Media Function ([MF](/mobilnisite/slovnik/mf/)) a Key Management Function (KMF) na síťové straně. Pracovní postup začíná tím, že DASH klient získá MPD, která obsahuje informace o dostupných mediálních streamech, včetně podrobností o jejich šifrování a URL příslušné KMF. IRD tyto informace využívá k navázání zabezpečené relace s KMF, přičemž používá protokoly jako jsou mechanismy pro doručování klíčů 3GPP Common Encryption ([CENC](/mobilnisite/slovnik/cenc/)). KMF autentizuje IRD (a tím i uživatele/zařízení) a doručí potřebné dešifrovací klíče, jako jsou Content Encryption Keys (CEK), často zabalené pomocí klíčů specifických pro daný IRD.

Po přijetí šifrovaného mediálního segmentu IRD provede dešifrování pomocí získaných CEK. Proces dešifrování dodržuje standardizovaná šifrovací schémata jako [ISO](/mobilnisite/slovnik/iso/) Common Encryption (schémata 'cenc' nebo 'cbcs'). Po dešifrování jsou komprimovaná mediální data (např. kódovaná pomocí H.264/[AVC](/mobilnisite/slovnik/avc/) nebo H.265/HEVC) předána příslušnému hardwarovému nebo softwarovému dekodéru pro dekompresi, což vede k nezpracovaným audio a video snímkům připraveným pro vykreslení. IRD je klíčovou komponentou pro vynucování digitální správy práv (DRM), protože zajišťuje, že pouze autorizovaní klienti s platnými klíči mají přístup k nešifrovanému obsahu. Její integrace do streamovacích standardů 3GPP zajišťuje standardizovanou, interoperabilní a bezpečnou metodu pro doručování prémiových multimediálních služeb přes mobilní sítě.

## K čemu slouží

IRD byl zaveden, aby řešil potřebu standardizované, bezpečné a efektivní klientské komponenty pro chráněné streamování médií v ekosystémech 3GPP. Před jeho formální definicí streamovací služby často spoléhaly na proprietární DRM klienty a mechanismy doručování, což vedlo k fragmentaci, zvýšené složitosti pro výrobce zařízení a poskytovatele obsahu a potenciálním bezpečnostním zranitelnostem kvůli nestandardním implementacím.

Vytvoření IRD, zejména od Release 13 dále, bylo motivováno explozivním růstem spotřeby mobilního videa a požadavkem na jednotný rámec v rámci specifikací 3GPP Dynamic Adaptive Streaming over HTTP (DASH). Řeší problém zabezpečeného propojení dešifrování obsahu s konkrétní streamovací relací a autorizací klienta. Definováním jasné funkční entity a jejích rozhraní (např. ke KMF) umožnilo 3GPP interoperabilní zabezpečení mezi síťovými službami správy klíčů a širokou škálou klientských zařízení.

Tato standardizace byla klíčová pro umožnění komerčních služeb jako mobilní TV, prémiové video na vyžádání a streamování živých událostí přes sítě LTE a 5G. Poskytuje poskytovatelům obsahu spolehlivý mechanismus pro ochranu jejich aktiv a zároveň dává výrobcům zařízení jasný návod pro implementaci kompatibilních řetězců pro přehrávání médií s integrovanou bezpečností. Koncept IRD pomáhá odklonit se od 'black box' DRM řešení směrem k transparentnějšímu bezpečnostnímu modelu založenému na standardech, který je zásadní pro škálovatelné, multiplatformní mediální služby.

## Klíčové vlastnosti

- Přijímá a zpracovává šifrované DASH mediální segmenty
- Komunikuje s Key Management Function (KMF) pro zabezpečené získání klíčů
- Provádí dešifrování pomocí standardizovaných schémat Common Encryption (CENC)
- Integruje se s řetězcem pro dekódování médií na klientovi
- Vynucuje relací založenou digitální správu práv (DRM)
- Funguje jako součást architektury 3GPP M4S (Media Streaming)

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [IRD na 3GPP Explorer](https://3gpp-explorer.com/glossary/ird/)
