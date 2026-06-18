---
slug: "parameter"
url: "/mobilnisite/slovnik/parameter/"
type: "slovnik"
title: "Parameter – Parameter"
date: 2024-01-01
abbr: "Parameter"
fullName: "Parameter"
category: "Management"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/parameter/"
summary: "Základní datový prvek v rámci specifikací 3GPP, často představující konfigurovatelnou hodnotu, identifikátor nebo nastavení definující chování sítě nebo zařízení. V konkrétních kontextech, jako je UIC"
---

Parametr je základní datový prvek v rámci specifikací 3GPP, který často představuje konfigurovatelnou hodnotu, identifikátor nebo nastavení definující chování sítě nebo zařízení.

## Popis

V ekosystému 3GPP je 'Parametr' obecný, ale základní koncept představující diskrétní část dat, která řídí, popisuje nebo je zpracovávána síťovou funkcí, protokolovou entitou nebo uživatelským zařízením. Parametry jsou atomické jednotky konfigurace signalizace a správy stavu. Mohou to být celá čísla, bitové řetězce, výčtové typy nebo – jak je výslovně uvedeno ve specifikacích jako 31.213 – hexadecimální hodnoty. Jejich rozsah je obrovský a pokrývá vše od časovačů řízení rádiových zdrojů a prahových hodnot pro předávání spojení až po kryptografické klíče a identifikátory účastníků.

Z architektonického hlediska jsou parametry definovány v rámci jednotek protokolových dat ([PDU](/mobilnisite/slovnik/pdu/)), objektů správy ([MO](/mobilnisite/slovnik/mo/)) nebo databázových polí. Jsou vyměňovány přes standardizovaná rozhraní (např. N1, [N2](/mobilnisite/slovnik/n2/), [X2](/mobilnisite/slovnik/x2/), S1) prostřednictvím konkrétních zpráv. Například v Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) jsou parametry jako Tracking Area Identity ([TAI](/mobilnisite/slovnik/tai/)) nebo Security Context přenášeny v rámci signalizačních zpráv. V Access Stratum obsahují zprávy [RRC](/mobilnisite/slovnik/rrc/) parametry pro konfiguraci šířky pásma fyzické vrstvy, režimů [MIMO](/mobilnisite/slovnik/mimo/) nebo přidělení prostředků pro plánování. V systémech správy sítě jsou parametry modelovány jako Managed Objects a lze je číst nebo zapisovat pomocí protokolů jako NETCONF/YANG nebo rozhraní založených na CORBA.

Konkrétní a kritickou aplikací je použití v rámci aplikace UICC a USIM, jak je podrobně popsáno v 3GPP TS 31.213. Zde se pojem 'Parametr' často vztahuje k hodnotě reprezentované v hexadecimálním formátu používané pro zabezpečené operace. To zahrnuje autentizační parametry jako RAND (náhodná výzva) a RES (odpověď), kryptografické klíče (K, CK, IK) a konfigurační data služeb. USIM funguje jako zabezpečené úložiště parametrů a mobilní zařízení (ME) nebo síť tyto parametry vyžaduje k provádění funkcí, jako je vzájemná autentizace (AKA), šifrování a ochrana integrity. Hexadecimální reprezentace je vhodný a jednoznačný formát pro binární data, který zajišťuje konzistentní interpretaci na různých hardwarových a softwarových platformách.

## K čemu slouží

Účelem definice parametrů v 3GPP je vytvořit přesný a jednoznačný jazyk pro interoperabilitu. Mobilní síť je masivně distribuovaný systém se zařízeními od stovek dodavatelů; parametry slouží jako společná slovní zásoba, která umožňuje základnové stanici od dodavatele A nakonfigurovat telefon od dodavatele B. Standardizace názvu, formátu, kódování a přípustných hodnot každého parametru je nezbytná pro spolehlivou komunikaci a konzistentní chování sítě.

V konkrétním kontextu parametrů USIM (hexadecimální hodnoty) je účelem zabezpečení a spolehlivé uložení. USIM je odolný hardwarový prvek navržený pro bezpečné ukládání citlivých dat účastníka. Reprezentace autentizačních klíčů a výzev jako binárních hodnot kódovaných hexadecimálně umožňuje jejich bezpečné generování, přenos a zpracování v rámci kryptografických algoritmů. Tento přístup izoluje kritické bezpečnostní parametry od méně zabezpečeného hlavního operačního systému zařízení a poskytuje základní důvěryhodný prvek pro celou síť. Bez takto standardizovaných parametrů by byla nemožná bezpečná autentizace, soukromí účastníků a přenositelnost služeb.

## Klíčové vlastnosti

- Atomický datový prvek definující konfiguraci a stav sítě/zařízení.
- Může být různých typů: celé číslo, řetězec, výčtový typ nebo hexadecimální hodnota.
- Zapouzdřen v rámci protokolových zpráv pro výměnu přes standardizovaná rozhraní.
- Kritický pro interoperabilitu mezi síťovými prvky od různých dodavatelů.
- V kontextu USIM často hexadecimální hodnota používaná pro autentizaci (RAND, RES, AUTN) a uložení klíčů.
- Modelován jako Managed Objects pro konfigurační správu a správu poruch a výkonu (CM, FM, PM).

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TS 31.213** (Rel-18) — Test specification for (U)SIM

---

📖 **Anglický originál a plná specifikace:** [Parameter na 3GPP Explorer](https://3gpp-explorer.com/glossary/parameter/)
