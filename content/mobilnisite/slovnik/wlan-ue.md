---
slug: "wlan-ue"
url: "/mobilnisite/slovnik/wlan-ue/"
type: "slovnik"
title: "WLAN-UE – WLAN User Equipment"
date: 2025-01-01
abbr: "WLAN-UE"
fullName: "WLAN User Equipment"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/wlan-ue/"
summary: "Uživatelské zařízení definované 3GPP, schopné přistupovat ke službám prostřednictvím bezdrátové lokální sítě (WLAN). Představuje formální integraci zařízení s podporou Wi-Fi do systémové architektury"
---

WLAN-UE je uživatelské zařízení definované standardem 3GPP, které je schopné přistupovat ke službám prostřednictvím bezdrátové lokální sítě (WLAN) a představuje formální integraci zařízení s podporou Wi-Fi do systémové architektury 3GPP.

## Popis

WLAN-UE je formální komponenta architektury 3GPP zavedená za účelem propojení buněčných a [WLAN](/mobilnisite/slovnik/wlan/) přístupových technologií. Označuje jakékoli uživatelské zařízení (UE), které disponuje WLAN rádiovými schopnostmi (např. Wi-Fi) a implementuje potřebné protokoly 3GPP pro interakci s jádrem sítě prostřednictvím důvěryhodné nebo nedůvěryhodné WLAN přístupové sítě. Nejde pouze o běžného Wi-Fi klienta; jedná se o UE, které podporuje specifické postupy definované 3GPP pro autentizaci, autorizaci, řízení politik a potenciálně i kontinuitu IP relací při přechodu mezi přístupem 3GPP a WLAN. Tento koncept je klíčový pro funkce jako Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) a později Non-Seamless WLAN Offload ([NSWO](/mobilnisite/slovnik/nswo/)) či IP Flow Mobility ([IFOM](/mobilnisite/slovnik/ifom/)).

Z architektonického hlediska WLAN-UE komunikuje s WLAN přístupovou sítí (WLAN [AN](/mobilnisite/slovnik/an/)) pomocí standardních protokolů [IEEE](/mobilnisite/slovnik/ieee/) 802.11. Pro integraci s 3GPP komunikuje s entitami jádra sítě prostřednictvím rozšířené brány paketových dat (ePDG) v případě nedůvěryhodného přístupu nebo přímo prostřednictvím důvěryhodné WLAN přístupové brány ([TWAG](/mobilnisite/slovnik/twag/)) v případě důvěryhodného přístupu. UE musí podporovat metody Extensible Authentication Protocol ([EAP](/mobilnisite/slovnik/eap/)), konkrétně EAP-AKA nebo EAP-AKA', pro autentizaci vůči jádru sítě 3GPP (server HSS/AAA). Také provádí politiky přijaté ze sítě, například od serveru ANDSF, aby mohlo činit inteligentní rozhodnutí o výběru přístupu mezi sítěmi 3GPP a WLAN.

Jeho role přesahuje rámec pouhé konektivity. WLAN-UE je klíčovým prvkem pro přesměrování, rozdělování a agregaci provozu. Umožňuje operátorům řídit přetížení sítě přesunem datového provozu na WLAN, při zachování kontroly nad předplatným uživatele a kvalitou služeb. Chování UE se řídí specifikacemi 3GPP, což zajišťuje standardizovanou interoperabilitu mezi zařízeními od různých výrobců a sítěmi operátorů. Tento krok byl zásadní pro to, aby se Wi-Fi stalo spravovaným rozšířením služby mobilního širokopásmového připojení.

## K čemu slouží

Koncept WLAN-UE byl vytvořen, aby formálně uznal a standardizoval roli zařízení s podporou Wi-Fi v rámci ekosystému 3GPP. Před jeho zavedením byl přístup Wi-Fi zcela oddělen od mobilního jádra sítě, což vedlo k nesourodému uživatelskému zážitku s oddělenými přihlašovacími údaji, účtováním a bezpečnostními profily. Primární problém, který řeší, je integrace všudypřítomné, ale nespravované technologie WLAN do bezpečného, na předplatném založeného a politikami řízeného prostředí mobilní sítě.

Historicky operátoři vnímali WLAN jako konkurenční a nespravovanou přístupovou technologii. Standardizace WLAN-UE, začínající ve vydání 8 (Release 8), byla motivována potřebou dostat WLAN pod kontrolu operátora. To umožnilo plynulou autentizaci pomocí SIM karty (prostřednictvím EAP-AKA), jednotné účtování a aplikaci konzistentních bezpečnostních a řídicích politik napříč buněčným i Wi-Fi přístupem. Řešila tak omezení plynoucí z existence dvou oddělených komunikačních komor a umožnila nové funkce, jako je přesměrování provozu iniciované sítí pro uvolnění přetížení buněčné sítě a poskytnutí robustnější kombinované nabídky služeb.

Vytvoření entity WLAN-UE poskytlo základní definici na straně terminálu pro veškerou následnou práci na propojení a integraci 3GPP a WLAN. Definovalo zařízení jako bod vynucování politik a koncový bod připojení s duálním zásobníkem, čímž připravilo cestu pro sofistikovanější integraci, jako je důvěryhodný WLAN přístup založený na S2a v pozdějších vydáních, a směřovalo k principům jednotného, na přístupu nezávislého jádra sítě v 5G.

## Klíčové vlastnosti

- Podporuje autentizaci založenou na 3GPP přes WLAN pomocí EAP-AKA/AKA'
- Může komunikovat s jádrem sítě prostřednictvím důvěryhodné (TWAG) nebo nedůvěryhodné (ePDG) WLAN přístupové brány
- Implementuje klientskou funkcionalitu pro příjem a aplikaci politik ANDSF
- Umožňuje Non-Seamless WLAN Offload (NSWO) pro přesměrování IP provozu
- Podporuje IP Flow Mobility (IFOM) a MAPCON pro simultánní vícepřístupová PDN připojení
- Slouží jako bod vynucování politik pro výběr přístupu a směrování provozu řízené sítí

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [EPDG – Evolved Packet Data Gateway](/mobilnisite/slovnik/epdg/)

## Definující specifikace

- **TS 29.234** (Rel-11) — WLAN-3GPP Interworking Stage-3 Protocol
- **TS 33.234** (Rel-19) — 3GPP-WLAN Interworking Security

---

📖 **Anglický originál a plná specifikace:** [WLAN-UE na 3GPP Explorer](https://3gpp-explorer.com/glossary/wlan-ue/)
