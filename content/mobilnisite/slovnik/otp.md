---
slug: "otp"
url: "/mobilnisite/slovnik/otp/"
type: "slovnik"
title: "OTP – One Time Password"
date: 2025-01-01
abbr: "OTP"
fullName: "One Time Password"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/otp/"
summary: "Bezpečnostní mechanismus, kdy heslo platí pouze pro jednu přihlašovací relaci nebo transakci, poskytující silné ověření a ochranu proti opakovaným útokům (replay attacks). V 3GPP se používá pro zabezp"
---

OTP je bezpečnostní mechanismus, kdy heslo platí pouze pro jednu přihlašovací relaci nebo transakci, používaný v 3GPP pro zabezpečení služeb jako MMS a ověřování uživatele.

## Popis

One Time Password (OTP, jednorázové heslo) je autentizační přihlašovací údaj platný pro jedno použití nebo krátký časový interval, po jehož uplynutí se stane neplatným. V systémech 3GPP se mechanismy OTP používají pro zvýšení zabezpečení přístupu ke službám, zejména u přidaných hodnotových služeb, kde tradiční statická hesla nepostačují. OTP je typicky generováno autentizačním serverem a doručeno do zařízení uživatele přes kanál mimo primární přenosovou cestu (out-of-band channel), například pomocí [SMS](/mobilnisite/slovnik/sms/) (Short Message Service) nebo vyhrazené mobilní aplikace. Uživatel pak toto OTP předloží poskytovateli služby k dokončení procesu ověření.

Z architektonického hlediska zahrnuje framework OTP v 3GPP několik klíčových komponent: uživatelské zařízení (UE), které OTP přijímá, servisní platformu (např. [MMS](/mobilnisite/slovnik/mms/) Center, aplikační server) vyžadující ověření, a server pro generování a validaci OTP. Tento server je často integrován s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo samostatným serverem pro autentizaci, autorizaci a účtování ([AAA](/mobilnisite/slovnik/aaa/) server). Proces začíná, když uživatel zahájí transakci; servisní platforma požádá server pro generování o OTP. Server vytvoří kryptograficky zabezpečené, časově nebo událostně synchronizované heslo a odešle jej na registrované mobilní číslo uživatele. Uživatel obdržené OTP odešle servisní platformě, která jej ověří proti serveru před udělením přístupu.

OTP funguje tak, že eliminuje riziko spojené s opakovaným použitím statického tajemství. Protože je každé heslo jedinečné a pomíjivé, zachycené přihlašovací údaje z předchozí transakce nelze znovu použít (replay). V 3GPP specifikace jako TS 31.113 definují mechanismus OTP pro zabezpečení načítání MMS, čímž brání neoprávněnému přístupu k multimediálním zprávám. Systém používá algoritmy jako Time-based One-Time Password (TOTP) nebo HMAC-based One-Time Password (HOTP), které často využívají sdílené tajemství (shared secret seed) bezpečně uložené na serveru a v [SIM](/mobilnisite/slovnik/sim/) kartě nebo zařízení uživatele. Tato metoda poskytuje robustní druhý faktor ve schématech vícefaktorového ověřování, což výrazně posiluje zabezpečení pro mobilní obchod, bankovnictví a přístup k citlivým službám v rámci telekomunikačního ekosystému.

## K čemu slouží

OTP bylo zavedeno, aby řešilo zranitelnosti vlastní ověřování založenému na statických heslech, které jsou náchylné k odposlechu, phishingu a opakovaným útokům (replay attacks). Když mobilní sítě začaly nabízet citlivé služby jako multimediální zasílání zpráv, mobilní bankovnictví a přístup k prémiovému obsahu, potřeba silnějších mechanismů ověření uživatele se stala kritickou. Statická hesla, pokud jsou kompromitována, mohou vést k neoprávněnému využívání služeb, finančním ztrátám a narušení soukromí.

Primární problém, který OTP řeší, je zajištění, že i když je autentizační přihlašovací údaj zachycen, nemůže být znovu zneužít. To je obzvláště důležité pro transakce prováděné přes potenciálně nezabezpečené kanály. Motivací pro jeho standardizaci v rámci 3GPP bylo poskytnout konzistentní, interoperabilní a bezpečnou metodu pro poskytovatele služeb (jak síťové operátory, tak třetí strany), jak ověřovat uživatele bez nutnosti spoléhat se na složitou infrastrukturu veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)) na UE pro každou transakci.

Historicky jeho přijetí ve vydání Release 6 poskytlo základní bezpečnostní vrstvu pro rostoucí trh mobilních datových služeb. Řešilo omezení dřívějších jednoduchých heslových mechanismů definovaných pro služby jako [WAP](/mobilnisite/slovnik/wap/), a nabídlo dynamičtější a bezpečnější alternativu, která využívala schopnost mobilní sítě komunikovat přímo s uživatelským zařízením přes [SMS](/mobilnisite/slovnik/sms/). Tím vytvořila důvěryhodný kanál mimo primární přenosovou cestu (trusted out-of-band channel), což posílilo celkové zabezpečení pro mobilní aplikace a chránilo jak operátory, tak účastníky před podvody.

## Klíčové vlastnosti

- Přihlašovací údaj na jedno použití platný pro jednu transakci nebo krátký časový úsek
- Typicky doručován přes kanály mimo primární přenosovou cestu (out-of-band), jako SMS nebo mobilní aplikace
- Založen na kryptografických algoritmech (např. TOTP, HOTP) využívajících sdílená tajemství
- Integruje se s platformami služeb 3GPP, jako je MMS, pro zabezpečené načítání
- Poskytuje silnou ochranu proti opakovaným (replay) a odposlechovým útokům
- Podporuje dvoufaktorová a vícefaktorová schémata ověřování

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 33.700** — 3GPP TR 33.700

---

📖 **Anglický originál a plná specifikace:** [OTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/otp/)
