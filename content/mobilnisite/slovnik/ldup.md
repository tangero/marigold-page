---
slug: "ldup"
url: "/mobilnisite/slovnik/ldup/"
type: "slovnik"
title: "LDUP – LDAP Duplication/Replication/Update Protocols"
date: 2025-01-01
abbr: "LDUP"
fullName: "LDAP Duplication/Replication/Update Protocols"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ldup/"
summary: "LDUP označuje soubor protokolů a procedur specifikovaných 3GPP pro duplikaci, replikaci a aktualizaci dat uložených v adresářových informačních bázích (DIB) s využitím protokolu LDAP (Lightweight Dire"
---

LDUP je soubor protokolů 3GPP pro duplikaci, replikaci a aktualizaci adresářových dat s využitím LDAP, které zajišťuje synchronizovaná data napříč adresáři síťového managementu pro informace o účastnících, konfiguraci a politikách.

## Popis

Protokoly pro duplikaci/replikaci/aktualizaci [LDAP](/mobilnisite/slovnik/ldap/) (LDUP) představují rámec definovaný v rámci telekomunikačního managementu sítě ([TMN](/mobilnisite/slovnik/tmn/)) 3GPP a později architektury systému managementu ([MS](/mobilnisite/slovnik/ms/)). Specifikuje, jak synchronizovat data mezi více adresářovými informačními bázemi (DIB), což jsou hierarchické databáze často používané pro ukládání informací síťového managementu, jako jsou profily účastníků, konfigurace zařízení, servisní politiky a autentizační data. Základním využívaným protokolem je LDAP (Lightweight Directory Access Protocol), otevřený standard pro přístup a správu adresářových služeb. LDUP definuje konkrétní mechanismy pro počáteční duplikaci dat (zkopírování celé DIB), průběžnou replikaci (synchronizaci přírůstkových změn) a šíření aktualizací mezi adresářovými servery. Architektura typicky zahrnuje roli dodavatele (zdroj změn dat) a roli spotřebitele (příjemce). Změny provedené v DIB dodavatele jsou zachyceny, formátovány do operací aktualizace LDAP (jako přidání, změna, smazání) a přenášeny do jedné nebo více DIB spotřebitelů. LDUP specifikuje obsah replikačních dohod, které definují rozsah dat k synchronizaci (např. konkrétní podstromy), plán (např. průběžný, periodický) a politiky řešení konfliktů pro případ, kdy jsou stejná data změněna na dvou místech. Zahrnuje také mechanismy oznamování změn a zajišťuje konzistenci aktualizací a integritu dat v rámci distribuovaného adresářového systému. Tento proces je klíčový pro udržování jednotného logického pohledu na kritická síťová data napříč geograficky rozptýlenými nebo funkčně oddělenými systémy managementu, jako je například mezi správcem sítě ([NM](/mobilnisite/slovnik/nm/)) a více správci prvků ([EM](/mobilnisite/slovnik/em/)), nebo mezi různými doménami v rámci provozu poskytovatele služeb. Standardizací této replikace LDUP umožňuje odolnost proti poruchám (prostřednictvím redundantních adresářů), distribuci zátěže a konzistentní přístup k datům pro různé síťové funkce a servisní logiku.

## K čemu slouží

LDUP byl vytvořen, aby řešil kritickou potřebu konzistence a dostupnosti dat ve velkých, distribuovaných telekomunikačních sítích. Rané systémy síťového managementu často spoléhaly na proprietární nebo ad-hoc metody kopírování konfiguračních a účastnických dat mezi systémy, což vedlo k nekonzistencím, manuálním snahám o sjednocení a výpadkům služeb při poruchách. Jak sítě s příchodem inteligentních sítí, databází [HLR](/mobilnisite/slovnik/hlr/)/[HSS](/mobilnisite/slovnik/hss/) a řízení politik rostly v komplexnosti, stala se jediná možnost selhání pro adresářová data nepřijatelnou. Účelem LDUP je poskytnout standardizovaný, spolehlivý a škálovatelný mechanismus replikace dat založený na široce přijímaném protokolu [LDAP](/mobilnisite/slovnik/ldap/). Řeší problém synchronizace dat mezi entitami síťového managementu a zajišťuje, že všechny systémy pracují se stejnou sadou informací o účastnících, konfigurací síťových prvků a servisních politik. To je nezbytné pro kontinuitu služeb (pokud jeden adresář selže, může jej nahradit jiný), pro podporu distribuovaných architektur (jako je mít regionální kopie účastnických dat) a pro umožnění efektivního managementu více-dodavatelských sítí, kde různá zařízení využívají sdílená adresářová data. Jeho specifikace v rámci 3GPP zajistila interoperabilitu mezi systémy managementu od různých dodavatelů, čímž snížila náklady a složitost integrace. Využitím LDAP také umožnila telekomunikačním operátorům používat komerčně dostupnou technologii adresářových serverů, což podporovalo efektivitu a snižovalo závislost na dodavatelsky specifických řešeních. LDUP vytvořil základní vrstvu správy dat pro síťový management 3GPP a podpořil přechod k automatizovanějším a spolehlivějším provozním podpůrným systémům (OSS).

## Klíčové vlastnosti

- Standardizovaná replikace adresářových informačních bází (DIB) založených na LDAP v rámci systémů managementu 3GPP
- Definuje role dodavatele a spotřebitele pro jednosměrnou nebo multi-master replikaci
- Specifikuje protokoly pro počáteční úplnou duplikaci dat a přírůstkové šíření aktualizací
- Zahrnuje mechanismy pro oznamování změn, detekci konfliktů a politiky jejich řešení
- Umožňuje vysokou dostupnost a odolnost proti poruchám prostřednictvím synchronizovaných redundantních adresářů
- Podporuje škálovatelné distribuované architektury managementu pro velké sítě

## Související pojmy

- [LDAP – Lightweight Directory Access Protocol](/mobilnisite/slovnik/ldap/)
- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)

## Definující specifikace

- **TS 32.101** (Rel-19) — Management principles and high-level requirements

---

📖 **Anglický originál a plná specifikace:** [LDUP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ldup/)
