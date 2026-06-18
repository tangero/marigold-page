---
slug: "n3g"
url: "/mobilnisite/slovnik/n3g/"
type: "slovnik"
title: "N3G – Non-3GPP Message Gateway"
date: 2025-01-01
abbr: "N3G"
fullName: "Non-3GPP Message Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/n3g/"
summary: "Síťová funkce 5G Core Network, která směruje a zpracovává signalizační zprávy mezi jádrem sítě a externími ne-3GPP aplikačními servery nebo sítěmi. Slouží jako zabezpečená brána pro SMS, MMS a další s"
---

N3G je síťová funkce 5G Core Network, která slouží jako zabezpečená brána pro směrování signalizačních zpráv, jako jsou SMS a MMS, mezi jádrem sítě a externími ne-3GPP aplikačními servery nebo sítěmi.

## Popis

Non-3GPP Message Gateway (N3G) je síťová funkce v architektuře 5G Core (5GC), definovaná pro zpracování služeb založených na zprávách pro uživatelská zařízení (UE) připojená přes ne-3GPP přístupové sítě. Primárně komunikuje s funkcí pro službu krátkých zpráv (SMSF) a dalšími aplikačními funkcemi a slouží jako koncový a směrovací bod pro provoz zasílání zpráv (jako [SMS](/mobilnisite/slovnik/sms/) a [MMS](/mobilnisite/slovnik/mms/)), který pochází od nebo je určen pro UE využívající Wi-Fi nebo jiný necestulární přístup. N3G se nachází na hranici mezi důvěryhodným 5G jádrem a externími subjekty pro zasílání zpráv nebo staršími centry zasílání zpráv. Jejím klíčovým úkolem je adaptovat protokoly a zajistit zabezpečené a spolehlivé doručování zpráv bez ohledu na aktuální typ přístupu UE.

Architektonicky N3G komunikuje s několika funkcemi 5GC. Pro doručování SMS komunikuje se SMSF přes rozhraní typu služba (např. služba Nsmsf). Když je potřeba odeslat zprávu UE registrované přes ne-3GPP přístup, může SMSF vyvolat N3G. N3G následně určí vhodnou metodu doručení, která často zahrnuje zapouzdření SMS v rámci protokolu založeného na IP (jako [HTTP](/mobilnisite/slovnik/http/)/2 nebo jiné protokoly specifikované v TS 29.538) a jeho směrování přes [N3IWF](/mobilnisite/slovnik/n3iwf/) a rozhraní [N3AN](/mobilnisite/slovnik/n3an/) k cílovému UE. Zpracovává funkce jako ukládání a přeposílání zpráv, pokud je UE dočasně nedostupné, konverzi protokolů mezi staršími SMS protokoly (jako [MAP](/mobilnisite/slovnik/map/)) a rozhraními 5GC typu služba a uplatňování politik souvisejících se zasíláním zpráv. Pro UE se N3G jeví jako koncový bod pro jejich službu zasílání zpráv při připojení přes Wi-Fi, což jim umožňuje odesílat a přijímat zprávy bez aktivního 3GPP rádiového spojení.

Z bezpečnostního a provozního hlediska N3G zajišťuje, že služby zasílání zpráv přes ne-3GPP přístup podléhají stejným standardům autentizace, autorizace a ochrany soukromí jako přístup 3GPP. Ověřuje, že je UE řádně autentizováno v systému 5G (přes [AMF](/mobilnisite/slovnik/amf/) a [AUSF](/mobilnisite/slovnik/ausf/)), než přijme zprávy jeho jménem. N3G také hraje roli při propojování se staršími sítěmi 2G/3G/4G pro SMS, funguje jako brána, která překládá mezi protokoly Diameter nebo MAP používanými v předchozích generacích a rozhraními typu služba 5GC založenými na HTTP/2. To umožňuje plynulou kontinuitu zasílání zpráv při vývoji sítí. Její specifikace podrobně popisují přesné toky zpráv, zpracování chyb a interakce pro účtování potřebné pro podporu těchto služeb, což z ní činí nezbytnou součást pro poskytování všudypřítomného zasílání zpráv v konvergované síti 5G.

## K čemu slouží

N3G byla vytvořena za účelem rozšíření základních telekomunikačních služeb, zejména SMS, na UE, která jsou připojena výhradně nebo převážně přes ne-3GPP přístup jako Wi-Fi. V systémech před 5G byla SMS úzce spojena s okruhově nebo paketově přepínanými doménami cestulární rádiové sítě. S rostoucím rozšířením Wi-Fi volání a zařízení pouze pro přenos dat byla zřejmá potřeba standardizovaného způsobu doručování těchto služeb přes přístupy založené na IP bez nutnosti spoléhat se na návrat k 3GPP rádiu. N3G tento problém řeší tím, že poskytuje v jádru 5G vyhrazenou, zabezpečenou bránu pro provoz zasílání zpráv.

Jejím účelem je zajistit kontinuitu služeb a stejnou úroveň služeb pro zasílání zpráv napříč všemi typy přístupů, což je kritický požadavek pro služby jako dvoufaktorová autentizace, výstrahy a zasílání zpráv mezi osobami. Bez N3G by UE na Wi-Fi nemuselo být schopno přijímat důležité SMS zprávy, což by vedlo ke špatnému uživatelskému zážitku a narušilo mnoho autentizačních toků závislých na SMS. N3G také řeší architektonický posun v 5G směrem k jádru typu služba s rozhraními HTTP/2; funguje jako nezbytný adaptační bod mezi tímto novým jádrem a stávajícím, často starším světem externích serverů a protokolů pro zasílání zpráv. Centralizací této funkce zjednodušuje síťovou architekturu, zvyšuje bezpečnost uplatňováním konzistentních politik 5G a umožňuje operátorům nabízet jednotný portfoli služeb zasílání zpráv bez ohledu na to, jak se účastník k síti připojí.

## Klíčové vlastnosti

- Síťová funkce 5G Core Network pro zasílání zpráv přes ne-3GPP přístup
- Spolupracuje se SMSF pro doručování a směrování SMS
- Poskytuje adaptaci protokolů mezi rozhraními typu služba 5GC a staršími protokoly pro zasílání zpráv
- Podporuje ukládání a přeposílání zpráv pro nedostupná UE
- Umožňuje zabezpečené doručování SMS přes IPsec tunely přes N3IWF
- Integruje se s 5G autentizačními a politickými řídicími frameworky

## Související pojmy

- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)

## Definující specifikace

- **TS 24.244** (Rel-19) — Wireless LAN Control Plane Protocol
- **TS 29.538** (Rel-19) — MSGin5G Service API Specification

---

📖 **Anglický originál a plná specifikace:** [N3G na 3GPP Explorer](https://3gpp-explorer.com/glossary/n3g/)
