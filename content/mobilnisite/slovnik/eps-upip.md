---
slug: "eps-upip"
url: "/mobilnisite/slovnik/eps-upip/"
type: "slovnik"
title: "EPS-UPIP – EPS User-Plane Integrity Protection"
date: 2025-01-01
abbr: "EPS-UPIP"
fullName: "EPS User-Plane Integrity Protection"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/eps-upip/"
summary: "Bezpečnostní funkce zavedená v 3GPP specifikacích z éry 5G, která poskytuje ochranu integrity pro datový provoz uživatelské roviny v Evolved Packet System (EPS). Chrání data před manipulací a vkládací"
---

EPS-UPIP je bezpečnostní funkce EPS z éry 5G, která poskytuje ochranu integrity pro data uživatelské roviny přes rozhraní rádiového přístupu, aby je chránila před manipulací a vkládacími útoky.

## Popis

EPS User-Plane Integrity Protection (EPS-UPIP) je bezpečnostní vylepšení definované ve specifikacích 3GPP TS 24.301 ([NAS](/mobilnisite/slovnik/nas/)) a TS 24.501, zavedené za účelem poskytnutí ochrany integrity pro datové pakety uživatelské roviny (UP) v sítích EPS. Před jeho zavedením se EPS primárně spoléhalo na šifrování pro důvěrnost UP, zatímco ochrana integrity byla typicky aplikována pouze na signalizaci řídicí roviny (NAS a [RRC](/mobilnisite/slovnik/rrc/)). EPS-UPIP rozšiřuje ochranu integrity na samotná uživatelská data přenášená přes rádiový přístup mezi UE a eNodeB, čímž zajišťuje, že data nebyla útočníkem změněna, zopakována nebo vložena.

Funkce funguje tak, že UE a síť aplikují integritní algoritmus na datové pakety uživatelské roviny, čímž generují integritní značku (neboli [MAC](/mobilnisite/slovnik/mac/)), která je připojena k datům nebo s nimi asociována. Tento proces probíhá na vrstvě Packet Data Convergence Protocol (PDCP) pro rádiové rozhraní. Použitý integritní klíč je odvozen z existující hierarchie bezpečnostních klíčů EPS. Konkrétně využívá klíče odvozené z K_[eNB](/mobilnisite/slovnik/enb/), které samo pochází z K_[ASME](/mobilnisite/slovnik/asme/). Aktivace ochrany integrity UP je vyjednána během procedury příkazu bezpečnostního režimu mezi UE a sítí na základě síťových politik a schopností UE.

Z architektonického hlediska se na EPS-UPIP podílejí UE, eNodeB a [MME](/mobilnisite/slovnik/mme/). MME rozhoduje o aktivaci funkce na základě předplatitelských dat, lokální politiky a bezpečnostních schopností UE indikovaných při připojení. Skutečnou ochranu a verifikaci integrity provádějí entity PDCP v UE a eNodeB. Zavedení této funkce vyžadovalo aktualizace protokolu PDCP a řídicích procedur bezpečnostního režimu, aby byla podpořena vyjednávání a aktivace integritních algoritmů pro uživatelskou rovinu. Představuje významný posun směrem k přiblížení bezpečnosti EPS komplexnějšímu modelu 'vždy zapnuté' ochrany integrity, který byl představen v systémech 5G (NR).

## K čemu slouží

EPS-UPIP bylo zavedeno ve 3GPP Release 17, aby řešilo rostoucí bezpečnostní hrozby pro uživatelská data v mobilních sítích, zejména riziko aktivních útoků na rádiové rozhraní. Před Release 17 se bezpečnost uživatelské roviny EPS zaměřovala téměř výhradně na šifrování (důvěrnost), což ponechávalo data zranitelná vůči škodlivé manipulaci, vkládání nebo opakovaným útokům, které mohly poškodit datové toky nebo vložit škodlivý obsah bez detekce. Motivací byl zvýšený význam citlivých služeb (např. průmyslový IoT, finanční transakce, vzdálené operace) a snaha zvýšit úroveň zabezpečení 4G tak, aby bylo konzistentnější s principy 5G.

Jeho vytvoření bylo motivováno poznatky z návrhu 5G, kde je ochrana integrity uživatelské roviny výchozí a základní součástí bezpečnostní architektury. EPS-UPIP umožňuje operátorům zvýšit úroveň zabezpečení jejich stávajících nasazení EPS, zejména pro kritický IoT a podnikové služby, aniž by vyžadovalo úplnou migraci na 5G. Řeší problém autenticity a integrity dat pro rozsáhlou instalovanou základnu zařízení a sítí LTE a uzavírá tak známou bezpečnostní mezeru. Funkce je součástí širší pracovní položky 'vylepšení bezpečnosti EPS' zaměřené na zpětný přenos klíčových bezpečnostních funkcí 5G do architektury EPS.

## Klíčové vlastnosti

- Poskytuje ochranu integrity pro datové pakety uživatelské roviny přes rádiové rozhraní LTE-Uu
- Funguje na vrstvě PDCP s využitím integritních algoritmů (např. 128-NIA)
- Používá integritní klíče odvozené z existující hierarchie klíčů EPS (K_eNB)
- Aktivace je vyjednána prostřednictvím procedur Security Mode Command na základě síťové politiky
- Chrání uživatelskou rovinu před manipulací s daty, vkládacími a opakovacími útoky
- Přibližuje bezpečnost EPS standardům 5G a umožňuje konzistentní zabezpečení pro smíšená nasazení

## Definující specifikace

- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification

---

📖 **Anglický originál a plná specifikace:** [EPS-UPIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/eps-upip/)
