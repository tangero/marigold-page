---
slug: "gip"
url: "/mobilnisite/slovnik/gip/"
type: "slovnik"
title: "GIP – Generic IP access"
date: 2025-01-01
abbr: "GIP"
fullName: "Generic IP access"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gip/"
summary: "Standardizovaný mechanismus v subsystému IP multimedia (IMS), který umožňuje uživatelskému zařízení získat IP konektivitu pro služby IMS prostřednictvím jakékoli IP přístupové sítě, jako je WLAN nebo"
---

GIP je standardizovaný mechanismus IMS, který umožňuje uživatelskému zařízení získat IP konektivitu pro služby IMS prostřednictvím jakékoli IP přístupové sítě, čímž odděluje doručování služeb od paketové domény 3GPP.

## Popis

Generic IP access (GIP, obecný IP přístup) je koncept a architektonický princip v rámci subsystému IP multimedia (IMS) 3GPP definovaný v technických specifikacích jako TS 26.114 (Multimediální telefonie; Zpracování a interakce médií). Odkazuje na schopnost IMS poskytovat multimediální služby přes jakoukoli IP přístupovou síť, nikoli výhradně přes paketové (PS) domény definované 3GPP, jako jsou [GPRS](/mobilnisite/slovnik/gprs/), UMTS nebo LTE. Základní myšlenkou je, že jádrová síť IMS (zahrnující [CSCF](/mobilnisite/slovnik/cscf/), [HSS](/mobilnisite/slovnik/hss/) atd.) je na přístupu nezávislá; poskytuje služby, pokud má uživatelské zařízení (UE) IP připojení, které dosáhne do sítě IMS, bez ohledu na to, jak je toto IP připojení navázáno. To může být prostřednictvím mobilní sítě 3GPP, sítě Wi-Fi (jak je definováno v IMS over WLAN), pevného broadbandového připojení nebo i jiných bezdrátových technologií.

Architektonicky je GIP umožněn návrhem IMS, který jako základní signalizační protokol používá SIP (Session Initiation Protocol) přes IP. [P-CSCF](/mobilnisite/slovnik/p-cscf/) (Proxy-Call Session Control Function) je vstupním bodem do IMS a může být objeveno zařízením UE prostřednictvím [DHCP](/mobilnisite/slovnik/dhcp/) nebo jiných mechanismů specifických pro přístupovou síť. Pro zařízení UE využívající obecný IP přístup (např. laptop v domácí síti Wi-Fi) musí nejprve získat lokální IP adresu z přístupové sítě (např. přes DHCP). Následně provede objevení P-CSCF, což pro přístup mimo 3GPP může zahrnovat použití plně kvalifikovaného názvu domény ([FQDN](/mobilnisite/slovnik/fqdn/)) nakonfigurovaného v zařízení nebo poskytnutého přístupovou sítí. Jakmile je kontaktován P-CSCF, standardní procedury registrace a navazování relací v IMS (pomocí SIP REGISTER a INVITE) probíhají přes tento obecný IP transport. Média pro službu (hlas, video) jsou také přenášena přes IP pomocí RTP/RTCP, směrována přes mediální funkce IMS podle potřeby.

Klíčové komponenty, které v scénáři GIP interagují, zahrnují IMS klienta v UE, IP infrastrukturu přístupové sítě (router, DHCP server), P-CSCF a jádro IMS. Zabezpečení je kritický aspekt; při použití nedůvěryhodného přístupu mimo 3GPP (jako je veřejná Wi-Fi) musí zařízení UE navázat bezpečnostní asociaci [IPsec](/mobilnisite/slovnik/ipsec/) se sítí IMS, typně ukončenou na Security Gateway (SEG) nebo na samotném P-CSCF, podle specifikací IMS pro nedůvěryhodný přístup. Role GIP je zásadní pro konvergenční vizi IMS, protože umožňuje být společnou platformou pro doručování služeb pro konvergenci pevných a mobilních sítí ([FMC](/mobilnisite/slovnik/fmc/)), a umožňuje služby jako Voice over Wi-Fi (VoWiFi) a bezproblémovou kontinuitu služeb při pohybu uživatelů mezi různými typy IP sítí. Abstrahuje přístupovou vrstvu, což umožňuje jednotnou aplikaci servisní logiky.

## K čemu slouží

Generic IP access byl koncipován, aby přerušil těsné propojení mezi pokročilými multimediálními službami a mobilní radiovou přístupovou sítí 3GPP. Před IMS a GIP byly služby s přidanou hodnotou často uzavřeny v rámci specifických přístupových technologií (např. hlas v okruhově spínané doméně na GSM, paketová data na GPRS). Cílem IMS bylo vytvořit jedinou, znovupoužitelnou servisní vrstvu pro multimédia v reálném čase. GIP byla architektonickou odpovědí na otázku: "Jak můžeme doručit tyto služby IMS, pokud není uživatel připojen přes síť 3GPP?" Vyřešil problém nezávislosti na přístupu, což bylo klíčové pro konvergenci pevných a mobilních sítí a pro využití všudypřítomnosti IP sítí, jako jsou residenční broadband a veřejné Wi-Fi.

Historický kontext představuje snaha z poloviny let 2000 směrem k All-IP sítím a konkurence ze strany over-the-top (OTT) VoIP služeb, které mohly běžet na jakémkoli internetovém připojení. 3GPP potřebovalo strategii, aby jeho standardizované telekomunikační a messagingové služby byly konkurenceschopné tím, že budou dostupné také na jakékoli síti. GIP, standardizovaný počínaje Release 8 jako součást zralé architektury IMS, řešil omezení dřívějších pokusů, které byly specifické pro přístup. Umožnil operátorům nasadit IMS jednou a nabízet služby napříč svým mobilním, pevným a Wi-Fi pokrytím, čímž vytvořil jednotný uživatelský zážitek. To byl klíčový motivátor pro investice operátorů do IMS, protože zajistil jejich servisní platformě odolnost vůči vývoji přístupových technologií a umožnil nové obchodní modely, jako je nabídka volání v domácí zóně přes broadband.

## Klíčové vlastnosti

- Umožňuje přístup ke službám IMS přes jakoukoli IP síť (3GPP i mimo 3GPP)
- Využívá standardní protokoly IETF (SIP, RTP, IPsec) přes obecný IP transport
- Vyžaduje přístupově specifické procedury pro přidělování IP adres a objevování P-CSCF
- Podporuje bezpečnostní mechanismy pro důvěryhodné i nedůvěryhodné přístupové sítě
- Zásadní pro konvergenci pevných a mobilních sítí (FMC) a IMS přes Wi-Fi
- Na přístupu nezávislá servisní logika v jádru IMS (CSCF, HSS, AS)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling

---

📖 **Anglický originál a plná specifikace:** [GIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gip/)
