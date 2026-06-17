---
slug: "bdc"
url: "/mobilnisite/slovnik/bdc/"
type: "slovnik"
title: "BDC – Bootstrap Data Channel"
date: 2025-01-01
abbr: "BDC"
fullName: "Bootstrap Data Channel"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bdc/"
summary: "Zabezpečený komunikační kanál zřízený mezi zařízením a sítí během počátečních bootstrap procedur za účelem výměny citlivých konfiguračních dat. Poskytuje autentizovaný a šifrovaný přenos pro kritické"
---

BDC je zabezpečený, autentizovaný a šifrovaný kanál používaný během počátečního bootstrapu zařízení k výměně citlivých konfiguračních dat, než toto zařízení získá přístup k běžným síťovým službám.

## Popis

Bootstrap Data Channel (BDC) je základní bezpečnostní mechanismus v sítích 3GPP, který vytváří chráněnou komunikační cestu speciálně pro výměnu počátečních konfiguračních a autentizačních dat během bootstrap procedur zařízení. Tento kanál funguje ještě předtím, než zařízení naváže běžnou uživatelskou rovinu spojení, a vytváří tak zabezpečené prostředí, kde lze citlivé provizní informace přenášet bez rizika odposlechu nebo manipulace. BDC využívá stávající bezpečnostní protokoly a procedury správy klíčů k vytvoření této izolované komunikační cesty, čímž zajišťuje, že kritická bootstrap data zůstanou během celého provizního procesu důvěrná a chráněná z hlediska integrity.

Z architektonického hlediska BDC funguje mezi zařízením (User Equipment) a síťovými bootstrap funkcemi, typicky zahrnujícími Bootstrapping Server Function ([BSF](/mobilnisite/slovnik/bsf/)) a související síťové elementy. Zřízení kanálu následuje specifickou sekvenci, kde se zařízení nejprve autentizuje v síti pomocí dostupných přihlašovacích údajů, a poté vyjedná bezpečnostní parametry pro BDC relaci. Tento proces zahrnuje vzájemnou autentizaci mezi zařízením a síťovými bootstrap funkcemi, po níž následuje odvození relakčních klíčů speciálně pro ochranu BDC. Kanál podporuje výměnu dat jak po řídicí rovině, tak po uživatelské rovině, v závislosti na konkrétním bootstrap scénáři a síťové konfiguraci.

Klíčové komponenty implementace BDC zahrnují funkci BDC Session Management, která zajišťuje zřízení, správu a ukončení kanálu; BDC Security Context, který uchovává kryptografické materiály a bezpečnostní parametry pro relaci; a BDC Transport Layer, který poskytuje vlastní přenosové schopnosti pro data. Kanál podporuje různé transportní protokoly včetně [HTTP](/mobilnisite/slovnik/http/)/2 s TLS ochranou, což zajišťuje kompatibilitu s moderními webovými provizními systémy. BDC také integruje se stávajícími bezpečnostními architekturami 3GPP včetně procedur Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) a správy hierarchie klíčů.

BDC hraje klíčovou roli v bezpečném připojování (onboardingu) zařízení tím, že poskytuje chráněné prostředí pro výměnu citlivých informací, jako jsou počáteční certifikáty zařízení, přihlašovací údaje pro přístup k síti, konfigurace poskytovatele služeb a data bezpečnostních politik. Tento kanál zajišťuje, že i předtím, než zařízení získá plný síťový přístup, může bezpečně získat nezbytné přihlašovací údaje a konfigurace potřebné k navázání správné autentizace a autorizace pro následné síťové operace. Koncepce BDC zahrnuje mechanismy pro správu časového limitu relace, procedury pro opětovnou autentizaci a elegantní snížení funkčnosti v případě neshody bezpečnostních parametrů nebo výpadku sítě.

## K čemu slouží

Bootstrap Data Channel byl vytvořen, aby řešil významné bezpečnostní zranitelnosti v počátečních provizních procedurách zařízení, kdy byla citlivá konfigurační data přenášena přes nechráněné nebo minimálně chráněné kanály. V předchozích releasech 3GPP se bootstrap procedury často opíraly o základní bezpečnostní mechanismy, které byly nedostatečné pro moderní prostředí hrozeb, zvláště s rozšířením IoT zařízení a různorodých scénářů nasazení v sítích 5G. BDC poskytuje standardizovaný, robustní bezpečnostní rámec speciálně navržený pro kritickou bootstrap fázi, kdy jsou zařízení nejvíce zranitelná vůči útokům.

Historicky trpěly bootstrap procedury zařízení několika omezeními, včetně přenosu citlivých přihlašovacích údajů přes nešifrované kanály, absence vzájemné autentizace během počátečního provizování a nedostatečné ochrany proti útoku typu man-in-the-middle. Tyto zranitelnosti se stávaly stále problematičtějšími, jak se sítě vyvíjely k podpoře masivních IoT nasazení, síťového řezání (network slicing) a různorodých požadavků na služby. BDC tyto problémy řeší zřízením vyhrazeného, kryptograficky chráněného kanálu ještě před jakoukoli výměnou citlivých dat, čímž zajišťuje, že bootstrap procedury dodržují stejné bezpečnostní standardy jako běžné síťové operace.

Vytvoření BDC bylo motivováno potřebou jednotného, standardizovaného přístupu k zabezpečení bootstrap procedur napříč různými typy zařízení a síťovými nasazeními. Předchozí řešení byla často specifická pro dodavatele nebo implementovaná jako proprietární rozšíření, což vedlo k problémům s interoperabilitou a nekonzistentní úrovní zabezpečení. Standardizací BDC ve specifikacích 3GPP získává průmysl konzistentní rámec pro bezpečné připojování zařízení, který podporuje různé autentizační metody, zohledňuje různé schopnosti zařízení a bezproblémově integruje se stávajícími bezpečnostními architekturami 3GPP.

## Klíčové vlastnosti

- Poskytuje autentizovaný a šifrovaný přenos pro bootstrap data
- Vytváří bezpečnostní kontext před výměnou citlivých dat
- Podporuje vzájemnou autentizaci mezi zařízením a sítí
- Integruje se stávajícími bezpečnostními rámci 3GPP a správou klíčů
- Umožňuje zabezpečený přenos počátečních přihlašovacích údajů a konfigurací zařízení
- Podporuje transportní mechanismy jak řídicí, tak uživatelské roviny

## Definující specifikace

- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 26.264** (Rel-19) — IMS-based AR Real-Time Communication
- **TS 33.790** (Rel-19) — Security for Next-Gen Real-Time Communication Phase 2

---

📖 **Anglický originál a plná specifikace:** [BDC na 3GPP Explorer](https://3gpp-explorer.com/glossary/bdc/)
