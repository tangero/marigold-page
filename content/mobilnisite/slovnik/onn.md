---
slug: "onn"
url: "/mobilnisite/slovnik/onn/"
type: "slovnik"
title: "ONN – Onboarding Network"
date: 2026-01-01
abbr: "ONN"
fullName: "Onboarding Network"
category: "IoT"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/onn/"
summary: "Onboardingová síť (ONN) je důvěryhodná síť, typicky PLMN nebo SNPN, která zařízení poskytuje počáteční síťový přístup, aby mohlo bezpečně získat přihlašovací údaje pro svou cílovou síť služeb (např. S"
---

ONN je důvěryhodná síť, například PLMN nebo SNPN, která zajišťuje počáteční zabezpečený přístup, aby zařízení mohlo získat přihlašovací údaje pro svou cílovou síť služeb.

## Popis

Onboardingová síť (ONN) je základní komponentou rámce pro onboarding v 3GPP, konkrétně pro mechanismy jako [ON-SNPN](/mobilnisite/slovnik/on-snpn/). Konceptuálně jde o síť, ke které se zařízení může nejprve připojit, pokud nemá platné přihlašovací údaje pro zamýšlenou cílovou síť, což je často Samostatná Neprovozní Privátní Síť ([SNPN](/mobilnisite/slovnik/snpn/)). Primární úlohou ONN je poskytnout řízené, ověřené a zabezpečené prostředí, kde zařízení může navázat IP konektivitu a komunikovat se vzdáleným onboardingovým serverem nebo vydavatelem přihlašovacích údajů. Tento server je obvykle spojen s cílovou SNPN nebo s důvěryhodným poskytovatelem služeb.

Architektonicky může být ONN implementována jako vyhrazený slice Veřejné Pozemní Mobilní Sítě ([PLMN](/mobilnisite/slovnik/plmn/)), samostatná SNPN nakonfigurovaná pro onboarding, nebo dokonce neutrální hostitelská síť. Zahrnuje standardní funkce 5G core sítě, jako je [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/) a [UPF](/mobilnisite/slovnik/upf/), aby poskytovala základní datovou konektivitu. Klíčové je, že také komunikuje s Onboarding Server Function ([OSF](/mobilnisite/slovnik/osf/)) nebo podobnou entitou zodpovědnou za ověření zařízení a vydání přihlašovacích údajů. ONN pracuje se specifickou sadou identifikátorů sítě (PLMN ID nebo SNPN ID), které jsou zařízení předem nakonfigurována k rozpoznání nebo objevení jako důvěryhodného vstupního bodu pro onboarding.

Operační tok zahrnuje UE, která se pokouší zaregistrovat k síti za účelem onboardingu. Pokud cílová SNPN pro UE není dostupná nebo UE nemá přihlašovací údaje, může vyhledat a zvolit předkonfigurovanou ONN. Po úspěšném, avšak omezeném ověření u ONN (například pomocí obecných nebo zařízení specifických počátečních přihlašovacích údajů) je UE udělena omezená datová konektivita. Přes tento zabezpečený kanál UE naváže [HTTPS](/mobilnisite/slovnik/https/) nebo podobnou zabezpečenou relaci s onboardingovým serverem. Server ověří neměnnou identitu zařízení, potvrdí jeho oprávnění připojit se k cílové SNPN a následně jej vybaví potřebnými přihlašovacími údaji předplatného (SUPI, autentizační klíče). Po úspěšném provizionování se UE odpojí od ONN a použije nové přihlašovací údaje k provedení standardního registračního postupu se svou cílovou SNPN. ONN tak slouží jako zabezpečený prostředník, který izoluje potenciálně zranitelný proces provizionování od provozních sítí.

## K čemu slouží

Koncept ONN byl vytvořen, aby řešil kritický bootstrapový problém v rozsáhlých IoT a privátních síťových nasazeních: jak má zařízení bez předchozího vztahu k síti bezpečně získat přihlašovací údaje potřebné pro přístup k této síti? Bez ONN jsou možnosti omezené na nepraktické nebo nezabezpečené metody, jako je ruční konfigurace, fyzická rozhraní nebo předprovi­zionování všech zařízení u výrobce pro konkrétního zákazníka, což omezuje škálovatelnost a efektivitu dodavatelského řetězce.

Vytvoření konceptu ONN ve verzi 3GPP Release 17 bylo motivováno potřebou standardizovaného, na úrovni operátora a bezpečného bootstrapového mechanismu. Poskytuje důvěryhodnou 'vstupní zónu', která je oddělená od provozní SNPN, a zvyšuje tak bezpečnost tím, že omezuje případné útoky během fáze provizionování na onboardingové prostředí. Toto oddělení umožňuje operátorům SNPN soustředit se na svou klíčovou provozní bezpečnost bez vystavování své autentizační infrastruktury neověřeným zařízením. ONN umožňuje modely zero-touch provizionování, které jsou klíčové pro nákladově efektivní nasazení tisíců senzorů a aktuátorů v průmyslových prostředích. Nabízí také flexibilitu, protože jediná ONN (např. provozovaná výrobcem zařízení nebo mobilním operátorem) může sloužit jako onboardingová platforma pro zařízení určená pro mnoho různých SNPN vlastněných různými podniky.

## Klíčové vlastnosti

- Poskytuje počáteční, omezenou IP konektivitu zařízením bez přihlašovacích údajů pro cílovou síť.
- Může být implementována jako PLMN, SNPN nebo síťový slice vyhrazený pro onboarding.
- Komunikuje s důvěryhodnou funkcí Onboarding Server Function pro vydání přihlašovacích údajů.
- Používá specifické identifikátory sítě (PLMN ID/SNPN ID), které jsou schopna objevit onboardingem vybavená UE.
- Podporuje zabezpečené protokoly (např. TLS) pro komunikaci mezi zařízením a onboardingovým serverem.
- Izoluje proces vydávání přihlašovacích údajů od provozních sítí pro zvýšení bezpečnosti.

## Související pojmy

- [ON-SNPN – Onboarding Standalone Non-Public Network](/mobilnisite/slovnik/on-snpn/)
- [SNPN – Standalone Non-Public Network](/mobilnisite/slovnik/snpn/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service

---

📖 **Anglický originál a plná specifikace:** [ONN na 3GPP Explorer](https://3gpp-explorer.com/glossary/onn/)
