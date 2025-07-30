# Tabellenauszug Fehlerbehebung

## **Schritt 1: OCR-Ansicht für schlechte Extraktionsergebnisse öffnen**

Wenn die Ergebnisse des Tabellenauszugs-Trainings nicht gut sind:

1. Öffnen Sie die **OCR-Ansicht**, indem Sie auf das Lupensymbol mit **OCR** klicken.
2. Überprüfen Sie die Extraktionsergebnisse und sehen Sie, ob der OCR-Prozess die Datenerfassung verbessern kann.
3. Wenn die Ergebnisse immer noch schlecht aussehen, versuchen Sie ein anderes Dokument, um zu überprüfen, ob das Problem dokumentenspezifisch ist.
4. Wenn das Problem dokumentenspezifisch ist, verwenden Sie ein anderes Dokument für die Extraktion.
   * Wenn das Problem weiterhin besteht, befolgen Sie die nächsten Schritte.

## **Schritt 2: Überprüfen Sie die Verfügbarkeit von E-Text**

1. Überprüfen Sie, ob das Dokument über **E-Text** verfügt.
   * Sie können dies mit einem Tool wie **Adobe Acrobat** überprüfen.
   * Wenn das Dokument E-Text enthält, folgen Sie **Schritt 3.**
   * Wenn das Dokument keinen E-Text enthält, folgen Sie **Schritt 4.**

## **Schritt 3: E-Text-Extraktion aktivieren**

Wenn das Dokument E-Text enthält, haben Sie zwei Optionen:

1. **Aktivieren Sie die E-Text-Extraktion nur für diesen Lieferanten**:
   * Gehen Sie zurück zur **Dokumentenfeldvalidierung**.
   * Klicken Sie auf das Quadrat mit den drei Punkten in der linken Symbolleiste.
   * Aktivieren Sie hier die Option **E-Text verwenden, wenn verfügbar**, um sie nur für diesen Lieferanten zu aktivieren.
2. **Aktivieren Sie die E-Text-Extraktion für alle Lieferanten**:
   * Gehen Sie zu **Einstellungen** > **Dokumentenverarbeitung** > **OCR-Einstellungen**.
   * In diesem Abschnitt finden Sie die Option **E-Text verwenden, wenn verfügbar** und können sie für alle Lieferanten aktivieren.
3. Nach Aktivierung der E-Text-Extraktion versuchen Sie das **Tabellenauszugs-Training** erneut.
   * Wenn sich die Ergebnisse verbessern, ist das Problem behoben.
   * Wenn die Ergebnisse immer noch nicht gut sind, fahren Sie mit **Schritt 4** fort.

## **Schritt 4: Kein E-Text verfügbar - Ändern Sie die AI OCR-Version**

Wenn das Dokument keinen E-Text enthält:

1. Gehen Sie zu **Einstellungen** > **Dokumentenverarbeitung** > **OCR-Einstellungen**.
2. Ändern Sie die **AI OCR-Version** in eine andere Version.
3. Gehen Sie zurück zum **Tabellenauszugs-Training** und versuchen Sie es erneut.
4. Wenn das Ergebnis besser ist:
   * Überprüfen Sie andere Dokumente von verschiedenen Lieferanten, um sicherzustellen, dass die Extraktionsergebnisse für diese Lieferanten nicht von dieser Änderung beeinflusst werden.
   * **Seien Sie vorsichtig, da diese Änderung die Extraktionsergebnisse anderer Lieferanten beeinflussen kann.**
   * Diese Änderung kann sich auf andere Lieferanten auswirken, daher überprüfen Sie die Ergebnisse sorgfältig, um sicherzustellen, dass sie die Dokumentextraktionen anderer Lieferanten nicht negativ beeinflusst.
5. Wenn sich das Ergebnis nach Änderung der AI OCR-Version nicht verbessert hat, wenden Sie sich bitte an uns für weitere Unterstützung.
