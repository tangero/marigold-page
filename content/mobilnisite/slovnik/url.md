---
slug: "url"
url: "/mobilnisite/slovnik/url/"
type: "slovnik"
title: "URL – Universal Resource Locator"
date: 2026-01-01
abbr: "URL"
fullName: "Universal Resource Locator"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/url/"
summary: "URL je specifický typ URI, který poskytuje síťovou polohu a metodu přístupu k prostředku, jako je webová stránka nebo soubor. V 3GPP se URL používají pro přístup ke službám, doručování obsahu a řídicí"
---

URL je specifický typ URI, který poskytuje síťovou polohu a metodu přístupu k prostředku, což umožňuje zařízením jej získávat přes IP sítě pro přístup ke službám, doručování obsahu a řídicí operace v systémech 3GPP.

## Popis

Universal Resource Locator (URL) v 3GPP je podmnožinou [URI](/mobilnisite/slovnik/uri/), která určuje nejen identitu, ale také primární přístupový mechanismus a síťovou polohu prostředku. Definována standardy [IETF](/mobilnisite/slovnik/ietf/) typicky zahrnuje schéma (např. http, https, ftp), hostitele, port, cestu a řetězec dotazu. URL se používají napříč systémy 3GPP pro přístup ke službám, stahování obsahu a konfiguraci zařízení. Například při mobilním prohlížení URL odkazují na webové stránky; při streamování lokalizují mediální soubory; a při správě zařízení identifikují konfigurační servery. To umožňuje UE interagovat se síťovými prostředky pomocí standardizovaných internetových protokolů.

URL fungují tak, že poskytují úplnou adresu, kterou mohou klientské aplikace použít k získání prostředků. Když UE přistupuje ke službě – například přes [HTTP](/mobilnisite/slovnik/http/) – vytvoří HTTP požadavek pomocí komponent URL: schéma určuje protokol (HTTP), hostitel se přeloží na IP adresu přes [DNS](/mobilnisite/slovnik/dns/), port specifikuje koncový bod (výchozí 80 pro HTTP) a cesta označuje konkrétní prostředek na serveru. V kontextech 3GPP jsou URL často poskytovány zařízením prostřednictvím mechanismů jako [OMA](/mobilnisite/slovnik/oma/) Device Management ([DM](/mobilnisite/slovnik/dm/)) nebo Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)). Například URL může odkazovat na autorizační server pro obsah chráněný [DRM](/mobilnisite/slovnik/drm/) nebo na server politik pro pravidla QoS. Protokolový zásobník UE zpracovává překlad a připojení, zatímco aplikační vrstvy interpretují získaná data.

Klíčové architektonické prvky zahrnující URL zahrnují prohlížeč nebo klientské aplikace v UE, které iniciují požadavky; síťové funkce jako proxy nebo brány, které mohou URL zachytit nebo přesměrovat; a servisní platformy hostující prostředky. V IMS lze URL používat v SIP zprávách k odkazování na externí těla (např. nepřímý odkaz na obsah). Pro doručování obsahu jsou URL klíčové pro HTTP Adaptive Streaming (HAS), kde manifestní soubory obsahují URL pro mediální segmenty. Řídicí protokoly jako OMA DM používají URL k určení řídicích objektů nebo umístění aktualizací softwaru. Zabezpečení přístupu přes URL je zajištěno pomocí TLS (https) a autentizačních mechanismů, přičemž specifikace 3GPP často vyžadují zabezpečená schémata pro citlivé operace.

Role URL v sítích 3GPP je kritická pro doručování služeb a provozní podporu. Umožňuje bezproblémový přístup k internetovým a operátorem hostovaným službám a tvoří páteř mobilních datových zážitků. URL podporují dynamickou adaptaci obsahu tím, že odkazují na různé verze na základě schopností zařízení nebo stavu sítě. Také usnadňují automatizované procesy, jako je konfigurace zařízení při počátečním připojení nebo aktivaci služby. Využitím standardů URL zajišťuje 3GPP kompatibilitu s World Wide Web, což umožňuje mobilním sítím integrovat se s cloudovými službami, sítěmi pro distribuci obsahu a podnikovými aplikacemi. Tato univerzálnost je základem uživatelského zážitku u aplikací, streamování a webových služeb v 3G, 4G a 5G.

## K čemu slouží

Universal Resource Locator (URL) byl v 3GPP přijat, aby umožnil standardizovaný přístup k prostředkům přes IP sítě, a řešil tak potřebu mobilních zařízení interagovat s webovými a serverovými službami. Před jeho použitím se mobilní datové služby často spoléhaly na proprietární protokoly nebo omezené WAP brány, což omezovalo dostupnost obsahu a interoperabilitu. Jak se 3GPP vyvíjelo směrem k paketově přepínaným sítím v vydáních jako R99, vznikla potřeba podpory hlavních internetových protokolů, což vyžadovalo společné adresovací schéma pro lokalizaci prostředků. URL jako dobře zavedený webový standard poskytly způsob, jak sjednotit přístup k různorodému obsahu a službám, od jednoduchých webových stránek po komplexní aplikační servery.

URL řeší problém, jak mobilní zařízení konzistentním způsobem objevují a získávají síťové prostředky. Umožňuje operátorům nasazovat služby bez vlastního klientského softwaru, protože UE mohou používat vestavěné prohlížeče nebo standardní knihovny pro zpracování URL. Například při správě zařízení URL umožňují provizionování přes vzdušné rozhraní tím, že odkazují na konfigurační soubory. V multimédiích URL v seznamech stop umožňují adaptivní streamování napříč sítěmi. Bez URL by každá služba potřebovala vlastní adresovací mechanismus, což by zvyšovalo složitost a zhoršovalo uživatelský zážitek. URL také podporují škálovatelnost, protože prostředky mohou být distribuovány napříč více servery identifikovanými různými URL.

Historicky byla integrace URL do 3GPP hnána konvergencí mobilních a internetových technologií, zejména se zavedením trvalého datového připojení v UMTS. R99 přineslo rané použití pro WAP a MMS, ale pozdější vydání rozšířila URL na IMS, správu a řízení politik. Odstranila omezení dřívějších mobilních specifických schémat tím, že umožnila přímý přístup k internetovému obsahu, a podpořila tak inovace v mobilních aplikacích a službách. URL se staly nepostradatelnými pro vystavování služeb v 5G a edge computing, kde aplikace potřebují efektivně lokalizovat distribuované prostředky. Jejich pokračující vývoj podporuje nové případy užití, jako je VR streamování nebo získávání dat IoT.

## Klíčové vlastnosti

- Určuje přístupový protokol a síťovou polohu prostředků
- Podporuje schémata jako http, https, ftp pro různé služby
- Umožňuje získávání obsahu a přístup ke službám v mobilních prohlížečích a aplikacích
- Používá se při provizionování pro správu zařízení a doručování politik
- Usnadňuje adaptivní streamování prostřednictvím URL v manifestech
- Integruje se s DNS pro překlad hostitelů a vyrovnávání zatížení

## Související pojmy

- [URI – Universal Resource Identifier](/mobilnisite/slovnik/uri/)
- [HTTP – Hypertext Transfer Protocol](/mobilnisite/slovnik/http/)
- [DNS – Directory Name Service](/mobilnisite/slovnik/dns/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 23.804** (Rel-7) — SMS/MMS over IP Access Support
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.247** (Rel-19) — IMS Messaging Service Protocol Details
- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- **TS 24.528** (Rel-8) — Common Basic Communication Procedures for IMS Services
- **TS 24.542** (Rel-19) — SEAL Notification Management Protocol
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 24.628** (Rel-19) — Common Basic Communication Procedures in IMS
- … a dalších 57 specifikací

---

📖 **Anglický originál a plná specifikace:** [URL na 3GPP Explorer](https://3gpp-explorer.com/glossary/url/)
