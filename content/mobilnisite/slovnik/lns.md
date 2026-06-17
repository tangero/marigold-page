---
slug: "lns"
url: "/mobilnisite/slovnik/lns/"
type: "slovnik"
title: "LNS – L2TP Network Server"
date: 2025-01-01
abbr: "LNS"
fullName: "L2TP Network Server"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lns/"
summary: "Síťový prvek, který ukončuje L2TP tunely z L2TP Access Concentrator (LAC). Poskytuje rozhraní mezi paketovou jádrovou sítí 3GPP a externí IP sítí (např. internetem nebo podnikovým intranetem) pro přen"
---

LNS je síťový server, který ukončuje L2TP tunely z LAC a tvoří rozhraní mezi paketovým jádrem 3GPP a externí IP sítí pro přenos uživatelských dat.

## Popis

[L2TP](/mobilnisite/slovnik/l2tp/) Network Server (LNS) je klíčový uzel definovaný v raných paketových architekturách 3GPP, zejména pro [GPRS](/mobilnisite/slovnik/gprs/) a UMTS, který umožňuje spolupráci s externími IP sítěmi pomocí protokolu Layer 2 Tunneling Protocol (L2TP). Funguje jako koncový bod L2TP tunelů zřízených z L2TP Access Concentrator ([LAC](/mobilnisite/slovnik/lac/)), kterým je v kontextu 3GPP typicky Gateway GPRS Support Node (GGSN). LNS se nachází v privátní IP síti poskytovatele služeb nebo podniku. Jeho hlavní funkcí je de-encapsulace příchozích L2TP rámců z tunelu, extrakce dat PPP (Point-to-Point Protocol) session uživatele a směrování IP paketů do cílové IP sítě. Naopak pro downlinkový provoz zapouzdřuje IP pakety do PPP a L2TP rámců pro přenos zpět tunelem k uživatelskému zařízení (UE).

Architektonicky LNS stojí na hranici mezi mobilní sítí 3GPP a externí Packet Data Network (PDN). Datová cesta zahrnuje zřízení PDP Context mezi UE a GGSN. GGSN, fungující jako LAC, následně iniciuje L2TP tunel k předem nakonfigurovanému LNS. Uživatelský datový provoz je přenášen přes PPP session, která je sama přenášena uvnitř L2TP tunelu. Tím vzniká virtuální point-to-point spojení mezi UE a LNS, díky čemuž se UE jeví, jako by bylo přímo připojeno k síti LNS. LNS je zodpovědný za PPP vyjednávání (např. přiřazení IP adresy přes [IPCP](/mobilnisite/slovnik/ipcp/)), autentizaci (často pomocí [CHAP](/mobilnisite/slovnik/chap/) nebo PAP) a účtování (accounting) session účastníka.

Klíčové součásti funkčnosti LNS zahrnují správu koncového bodu L2TP tunelu, ukončení PPP session, IP směrování a často integrované [AAA](/mobilnisite/slovnik/aaa/) (Authentication, Authorization, and Accounting) klientské schopnosti pro komunikaci se serverem RADIUS. Jeho role byla klíčová pro umožnění bezpečného přístupu k podnikovým intranetům (předchůdce moderních VPN) a pro poskytovatelů internetových služeb ([ISP](/mobilnisite/slovnik/isp/)) pro poskytování přístupu k internetu mobilním účastníkům. Ukončením L2TP/PPP session přiřadí LNS UE IP adresu z podnikového/ISP fondu a stane se výchozí bránou pro provoz UE do externí sítě. Tento model poskytoval jasnou demarkační linii a standardizovanou metodu (L2TP) pro připojování mobilních sítí k externím IP služebním sítím před rozšířením GTP-based S8/SGi rozhraní a [IPsec](/mobilnisite/slovnik/ipsec/).

## K čemu slouží

LNS byl vytvořen k řešení problému bezpečného a transparentního připojování mobilních účastníků k externím IP sítím, zejména k podnikovým privátním sítím, v počátcích mobilních dat (GPRS/UMTS). Před standardizovaným tunelováním bylo poskytování přímého podnikového přístupu složité a nejisté. Účelem architektury L2TP/LNS bylo využít dobře zavedené protokoly PPP a L2TP z IETF k vytvoření virtuálního vytáčeného připojení (dial-up) přes IP-based mobilní jádrovou síť.

Tento přístup řešil několik omezení. Umožnil korporacím používat jejich stávající infrastrukturu pro vzdálený přístup (servery LNS) pro přijímání spojení od mobilních uživatelů bez zásadních změn. Poskytl vrstvu autentizace a autorizace oddělenou od HLR/AuC mobilní sítě. Dále vytvořil privátní tunel pro uživatelská data, čímž nabídl určitý stupeň důvěrnosti uvnitř páteřní sítě mobilního operátora. Model LNS byl ústřední pro nabídky služeb 'Wireless WAN' nebo 'Mobile VPN', které umožnily podnikovým uživatelům vzdálený přístup k emailu a interním aplikacím.

Motivací pro jeho specifikaci v 3GPP Rel-4 bylo poskytnout standardizované řešení pro spolupráci mezi sítěmi 3GPP a externími IP sítěmi, což zajišťovalo interoperabilitu více dodavatelů pro end-to-end datové služby. Jak se architektury 3GPP vyvíjely směrem k čistě IP modelu s GTP na rozhraní SGi a později s IPsec, závislost na L2TP a LNS pro obecný přístup k internetu poklesla. Koncept však položil základy pro zabezpečený přístup k paketovým datovým sítím a ovlivnil pozdější architektury, jako jsou eVPN a služby založené na IMS. Představoval klíčovou přemosťující technologii mezi zastaralým vytáčeným vzdáleným přístupem (dial-up remote access) a moderním mobilním broadbandem.

## Klíčové vlastnosti

- Ukončuje L2TP tunely iniciované GGSN (fungujícím jako LAC)
- Ukončuje PPP session od mobilních uživatelů, zajišťuje IPCP vyjednávání a přiřazení IP adresy
- Směruje de-encapsulovaný uživatelský IP provoz do/z externí Packet Data Network (PDN)
- Poskytuje rozhraní pro autentizaci, autorizaci a účtování (AAA), často přes RADIUS
- Umožňuje zabezpečený přístup k podnikovým intranetům (založený na APN)
- Definuje standardizovaný bod pro spolupráci mezi mobilními sítěmi 3GPP a externími IP služebními sítěmi

## Související pojmy

- [L2TP – Layer Two Tunneling Protocol](/mobilnisite/slovnik/l2tp/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [LNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lns/)
