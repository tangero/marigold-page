---
slug: "rpk"
url: "/mobilnisite/slovnik/rpk/"
type: "slovnik"
title: "RPK – Root Public Key"
date: 2025-01-01
abbr: "RPK"
fullName: "Root Public Key"
category: "Security"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/rpk/"
summary: "Kryptografický veřejný klíč používaný jako kořen důvěry v architekturách zabezpečení 3GPP, zejména pro zabezpečení aplikací a služeb UICC (SIM). Umožňuje bezpečné inicializování důvěry a ověřování při"
---

RPK je kořenový veřejný klíč, který slouží jako kryptografický základ důvěry v zabezpečení 3GPP, umožňuje ověření a integritu přihlašovacích údajů pro aplikace a služby UICC.

## Popis

Kořenový veřejný klíč (RPK) je základní kryptografický prvek v rámci bezpečnostních rámců 3GPP, který slouží jako vrchol hierarchie infrastruktury veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)). Jedná se o dlouhodobý, vysoce chráněný veřejný klíč, který působí jako konečná kotva důvěry pro ověřování digitálních podpisů a certifikátů v síti. RPK je typicky vestavěn do zabezpečených hardwarových prvků, jako je UICC (Universal Integrated Circuit Card) nebo zabezpečené enclavy zařízení, a používá se k ověření pravosti dalších klíčů a přihlašovacích údajů vydaných operátorem sítě nebo důvěryhodnými poskytovateli služeb. Jeho integrita je prvořadá, protože kompromitace RPK by podkopala celý bezpečnostní řetězec.

Architektonicky se RPK používá v protokolech a mechanismech definovaných ve specifikacích jako 3GPP TS 23.057 pro správu zabezpečených aplikací. Umožňuje bezpečnou inicializaci důvěry tím, že umožňuje entitám (např. mobilním zařízením, síťovým funkcím) ověřovat podpisy na certifikátech nebo datových objektech, které jsou podepsány odpovídajícím kořenovým privátním klíčem, bezpečně drženým vydávající autoritou. Tento proces ověření zajišťuje, že jsou přijímány pouze autorizované a nepozměněné softwarové, konfigurační nebo servisní přihlašovací údaje. RPK je často zřízen během výroby nebo počáteční personalizace UICC, čímž se zakládá hardwarově ukotvená důvěra, která přetrvává po celý životní cyklus zařízení.

V provozu RPK usnadňuje různé bezpečnostní služby, včetně zabezpečeného načítání a instalace aplikací na UICC, ověřování příkazů pro aktualizace přes vzdušné rozhraní ([OTA](/mobilnisite/slovnik/ota/)) a ověřování přihlašovacích údajů poskytovatele služeb. Když zařízení obdrží podepsaný příkaz nebo certifikát, použije uložený RPK k ověření podpisu. Pokud je ověření úspěšné, zařízení důvěřuje původu a integritě přijatých dat. Tento mechanismus je klíčový pro ochranu před pokusy škodlivých aktérů vložit neautorizované aplikace nebo narušit zabezpečení zařízení. Role RPK se rozšiřuje na zajištění zabezpečení služeb s přidanou hodnotou, jako jsou mobilní platby nebo správa identit, tím, že poskytuje ověřitelný řetězec důvěry od kořene ke klíčům specifickým pro danou službu.

## K čemu slouží

RPK byl zaveden, aby řešil rostoucí potřebu robustního, škálovatelného zabezpečení v mobilních sítích, zejména s rozšiřováním stahovatelných aplikací a služeb na UICC. Před jeho standardizací bezpečnostní mechanismy často spoléhaly na symetrické klíče nebo méně formalizované modely důvěry, které mohly být obtížně spravovatelné ve velkém měřítku a zranitelné vůči útokům na distribuci klíčů. RPK poskytuje standardizovaný kořen důvěry založený na veřejných klíčích, který zjednodušuje správu zabezpečených přihlašovacích údajů a umožňuje interoperabilitu mezi různými operátory a poskytovateli služeb.

Historicky, jak se UICC vyvíjely z jednoduchých [SIM](/mobilnisite/slovnik/sim/) karet pro autentizaci na platformy hostující více aplikací (např. pro bankovnictví, dopravu), stalo se zajištění integrity a pravosti těchto aplikací kritickým. RPK to řeší vytvořením kryptograficky silné kotvy důvěry, kterou lze použít k ověření podpisů na aplikačním kódu nebo datech, čímž se zabrání neautorizovaným úpravám nebo instalaci malwaru. Řeší omezení dřívějších přístupů tím, že umožňuje decentralizované vydávání přihlašovacích údajů při zachování centralizovaného kořene důvěry, což snižuje riziko kompromitace klíčů ve srovnání s rozsáhlou distribucí symetrických kořenových klíčů.

Dále RPK podporuje regulatorní a komerční požadavky na zabezpečené poskytování služeb, jako jsou ty v mobilních finančních službách nebo vládních programech ID. Poskytnutím ověřitelného řetězce důvěry pomáhá splňovat standardy compliance a buduje důvěru uživatelů v mobilní služby. Jeho zavedení ve vydání 10 bylo v souladu s posunem odvětví k otevřenějším, na aplikace bohatým prostředím UICC, kde musely být bezpečnostní základy jak silné, tak flexibilní.

## Klíčové vlastnosti

- Slouží jako kořenová kotva důvěry v hierarchiích PKI 3GPP
- Umožňuje ověření digitálních podpisů pro aplikace a data UICC
- Podporuje bezpečnou inicializaci důvěry pro aktualizace přes vzdušné rozhraní (OTA)
- Vestavěn do zabezpečeného hardwaru (např. UICC) pro odolnost proti neoprávněné manipulaci
- Usnadňuje interoperabilitu mezi operátory a poskytovateli služeb
- Používá se v protokolech pro správu zabezpečených aplikací a ověřování přihlašovacích údajů

## Související pojmy

- [OTA – Over The Air](/mobilnisite/slovnik/ota/)

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [RPK na 3GPP Explorer](https://3gpp-explorer.com/glossary/rpk/)
