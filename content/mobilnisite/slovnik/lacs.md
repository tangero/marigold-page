---
slug: "lacs"
url: "/mobilnisite/slovnik/lacs/"
type: "slovnik"
title: "LACS – Local Active Codec Set"
date: 2025-01-01
abbr: "LACS"
fullName: "Local Active Codec Set"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lacs/"
summary: "Seznam řečových kodeků specifický pro dané UE, které jsou aktuálně dostupné a nakonfigurované pro použití v hovoru s přepojováním okruhů. Je spravován sítí a odesílán UE, aby řídil, které kodeky lze b"
---

LACS je seznam dostupných a nakonfigurovaných řečových kodeků specifický pro dané UE, spravovaný sítí za účelem řízení výběru kodeku při sestavování hovoru v přepojování okruhů.

## Popis

Local Active Codec Set (LACS) je koncept správy a informační prvek používaný v 3GPP službách hlasu s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), specifikovaný v TS 28.062 pro účely řízení. Představuje množinu řečových kodeků, které je konkrétní uživatelské zařízení (UE) aktuálně schopno používat a které jsou sítí autorizovány pro daný hovor nebo kontext. LACS není statickou vlastností UE, ale dynamickým seznamem, který lze upravit signalizací ze sítě. Jádrová síť, typicky Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), určuje LACS a sděluje jej UE během procedur sestavování nebo modifikace hovoru.

Z procedurálního hlediska funguje LACS jako součást procesu negotiace kodeku. Při zahájení hovoru s přepojováním okruhů iniciovaného z mobilního zařízení nebo směřujícího k němu síť vyhodnotí různé faktory, jako je profil účastníka, síťové politiky a aktuální rádiové podmínky. Na základě tohoto vyhodnocení síť sestaví LACS – podmnožinu všech kodeků podporovaných UE – a zahrne jej do zprávy pro sestavení hovoru (např. zpráva SETUP nebo CALL CONFIRMED). UE pak musí omezit svůj výběr kodeku pro tento hovor pouze na ty kodeky, které jsou obsaženy v přijatém LACS. To síti umožňuje vynucovat politiky, upřednostňovat určité kodeky z důvodu efektivity šířky pásma nebo kvality a zajišťovat interoperabilitu se sítí volané strany.

Role LACS je klíčová pro efektivní správu rádiových prostředků a kvalitu služby v doméně CS. Řízením aktivní množiny může síť zabránit použití kodeků, které nejsou vhodné pro aktuální konfiguraci rádiového přenosu nebo které by spotřebovávaly nadměrnou šířku pásma. Také umožňuje funkce jako Transcoder Free Operation (TrFO) a Tandem Free Operation ([TFO](/mobilnisite/slovnik/tfo/)), kde lze LACS koordinovat mezi sítěmi, aby byl umožněn end-to-end kompatibilní kodek bez mezilehlého překódování. LACS je klíčovým parametrem v rámci Operation and Maintenance (O&M) pro monitorování a řízení výkonu hlasových služeb v síti.

## K čemu slouží

LACS byl vytvořen, aby vyřešil problém nekontrolovaného a neoptimálního výběru kodeku v mobilních hovorech s přepojováním okruhů. Rané systémy měly omezenou podporu kodeků, ale s vývojem sítí (např. od GSM [FR](/mobilnisite/slovnik/fr/)/[HR](/mobilnisite/slovnik/hr/) k [AMR](/mobilnisite/slovnik/amr/) a [AMR-WB](/mobilnisite/slovnik/amr-wb/)) začala UE podporovat více kodeků s různými přenosovými rychlostmi a úrovněmi kvality. Bez síťové kontroly by si UE mohlo vybrat kodek s vysokou přenosovou rychlostí nevhodný pro přetíženou buňku, nebo kodek nekompatibilní se vzdálenou stranou, což by vynutilo neefektivní překódování. Účelem LACS je dát síti centralizovanou, politikami řízenou kontrolu nad procesem negotiace kodeku.

Jeho zavedení bylo motivováno potřebou inteligentnějšího řízení rádiových prostředků a pokročilých funkcí pro kvalitu hlasu. Odstranil omezení statických, na terminálu založených seznamů kodeků tím, že umožnil síti dynamicky přizpůsobovat dostupnou množinu kodeků na základě aktuálních podmínek a služebních politik. To operátorům umožňuje optimalizovat využití spektra, zajistit konzistentní kvalitu služby a selektivně zavádět pokročilé hlasové služby jako širokopásmový audio (AMR-WB). LACS poskytuje mechanismus, kterým síť může 'navádět' chování UE, a zajišťuje tak, že jsou během fáze sestavování hovoru splněny celosíťové cíle pro efektivitu a interoperabilitu.

## Klíčové vlastnosti

- Dynamický seznam kodeků dostupných pro konkrétní CS hovor, řízený sítí
- Signalizován ze sítě (MSC) k UE během sestavování hovoru
- Omezuje výběr kodeku UE na autorizovanou podmnožinu
- Umožňuje síti vynucovat politiky pro použití kodeků a správu rádiových prostředků
- Podporuje pokročilé hlasové funkce jako Transcoder Free Operation (TrFO)
- Umožňuje adaptaci podporovaných kodeků na základě profilu účastníka a aktuálních síťových podmínek

## Definující specifikace

- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [LACS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lacs/)
