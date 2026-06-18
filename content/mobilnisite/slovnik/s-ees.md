---
slug: "s-ees"
url: "/mobilnisite/slovnik/s-ees/"
type: "slovnik"
title: "S-EES – Source Edge Enabler Server"
date: 2026-01-01
abbr: "S-EES"
fullName: "Source Edge Enabler Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/s-ees/"
summary: "Source Edge Enabler Server (S-EES) je funkční entita zavedená ve 3GPP Release 17 pro Edge Computing Enabler Layer (ECEL). Funguje jako důvěryhodný zprostředkovatel pro aplikační klienty, kterým zjišťu"
---

S-EES je funkční entita v Edge Computing Enabler Layer (vrstvě pro umožnění edge computingu) dle 3GPP, která funguje jako důvěryhodný zprostředkovatel pro klienty při zjišťování a přístupu k edge aplikačním serverům a jejich službám.

## Popis

Source Edge Enabler Server (S-EES) je klíčovou komponentou architektury Edge Computing Enabler Layer (ECEL) dle 3GPP, definované od Release 17. Funguje jako brána pro zjišťování služeb a přístup k nim pro aplikační klienty ([AC](/mobilnisite/slovnik/ac/)), kteří chtějí využít edge computingové prostředky. S-EES je typicky nasazen v síti operátora nebo v důvěryhodné doméně třetí strany. Jeho hlavní role spočívá v tom, že funguje jako důvěryhodný zprostředkovatel, na kterého se AC obrátí jako na první. AC poskytne S-EES popis služby nebo identifikátor edge aplikace, kterou chce využívat. S-EES následně konzultuje s dalšími entitami ECEL, primárně s Edge Configuration Server ([ECS](/mobilnisite/slovnik/ecs/)), aby zjistil vhodné instance Edge Application Server ([EAS](/mobilnisite/slovnik/eas/)), které mohou požadavek splnit. Tento proces zjišťování zohledňuje faktory jako je poloha klienta, síťové podmínky a schopnosti EAS, aby vybral optimální koncový bod. Jakmile je vhodný EAS identifikován, S-EES poskytne AC potřebné informace, jako je IP adresa nebo [FQDN](/mobilnisite/slovnik/fqdn/), a často i bezpečný přístupový token, aby mohlo být navázáno přímé nebo proxy připojení k EAS. Tato architektura abstrahuje složitost edge nasazení od aplikace, což umožňuje dynamické zjišťování služeb a plynulou mobilitu při pohybu klientů mezi různými oblastmi edge služeb. S-EES také hraje klíčovou roli v zabezpečení tím, že vynucuje ověřování a autorizační politiky pro AC, než odhalí podrobnosti o EAS, a tím chrání edge infrastrukturu před neoprávněným přístupem. Rozhraní s ECS využívá referenční bod En-1 a s AC referenční bod En-2, jak je specifikováno v TS 23.558.

## K čemu slouží

S-EES byl vytvořen, aby řešil výzvy spojené se zjišťováním služeb a přístupem k nim v distribuovaných edge computingových prostředích. Před jeho standardizací často vyžadoval přístup k edge aplikacím statickou konfiguraci nebo proprietární mechanismy zjišťování, které nebyly škálovatelné, bezpečné ani interoperabilní mezi různými operátory a dodavateli. Rozmach aplikací citlivých na latenci a náročných na šířku pásma, jako je rozšířená realita, průmyslová automatizace a videoanalytika, si vyžádal standardizovaný způsob, jak dynamicky najít a připojit se k nejbližší nebo nejvhodnější výpočetní instanci. S-EES tento problém řeší tím, že poskytuje centralizovaný, důvěryhodný kontaktní bod pro klienty. Odděluje klientskou aplikaci od fyzické a logické topologie edge sítě, což operátorům umožňuje nasazovat, spravovat a škálovat své edge prostředky nezávisle. Tato standardizace, zahájená v Release 17, byla motivována potřebou podpořit ekosystém interoperabilních edge služeb, snížit integrační složitost pro poskytovatele aplikací a zajistit bezpečné a efektivní využití edge computingové infrastruktury jako klíčového enableru pro sítě 5G a další generace.

## Klíčové vlastnosti

- Funguje jako primární koncový bod pro zjišťování a přístup pro aplikační klienty v architektuře ECEL
- Spolupracuje s Edge Configuration Server (ECS) při překladu identifikátorů služeb na konkrétní instance Edge Application Server (EAS)
- Poskytuje aplikačním klientům informace pro připojení k EAS a bezpečné přístupové tokeny
- Umožňuje podporu mobility klientů tím, že usnadňuje opětovné zjištění optimálních instancí EAS při změně polohy
- Vynucuje počáteční ověření a autorizaci aplikačních klientů před vystavením služby
- Abstrahuje detaily síťové a edge topologie od aplikační vrstvy

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [S-EES na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-ees/)
